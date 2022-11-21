import re
from flashtext import KeywordProcessor
from os import path as p


class HelperSensitiveCensor:
  """Classified email filter

  utility class which handles filter to test the incoming email text, detect if 
  the email might be classified, and additionally replace any sensitive text wi
  th censored ***** characters. 
  
  The list of confidential data is taken from: 
  (https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-personal-data_es)
  """  
  def __init__(self, list_words_to_filter : list, text_email: str):
    self.list_words_to_filter = list_words_to_filter
    self.text_email_original = text_email    
    self.text_email = text_email    
    self.dict_patterns = self.init_patters()
    self.keyword_processor_case_sensitive = KeywordProcessor(case_sensitive=True)
    self.keyword_processor_case_insensitive = KeywordProcessor(case_sensitive=False)
    self.list_key_words = self.initialize_key_word_processor()   
    self.wildcard = '*'
    self.contains_sensitive_data = False
        
    
  def init_ip_pattern(self):  
        ul = '\u00a1-\uffff'  # Unicode letters range (must not be a raw string).

        # IP patterns
        ipv4_re = r'(?:0|25[0-5]|2[0-4]\d|1\d?\d?|[1-9]\d?)(?:\.(?:0|25[0-5]|2[0-4]\d|1\d?\d?|[1-9]\d?)){3}'
        ipv6_re = r'\[?((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,'\
                  r'4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{'\
                  r'1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2['\
                  r'0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,'\
                  r'3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|['\
                  r'1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,'\
                  r'2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|((['\
                  r'0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2['\
                  r'0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:['\
                  r'0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2['\
                  r'0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,'\
                  r'5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\]?'

        # Host patterns
        hostname_re = r'[a-z' + ul + r'0-9](?:[a-z' + ul + r'0-9-]{0,61}[a-z' + ul + r'0-9])?'
        # Max length for domain name labels is 63 characters per RFC 1034 sec. 3.1
        domain_re = r'(?:\.(?!-)[a-z' + ul + r'0-9-]{1,63}(?<!-))*'
        tld_re = (
                r'\.'                                # dot
                r'(?!-)'                             # can't start with a dash
                r'(?:[a-z' + ul + '-]{2,63}'         # domain label
                r'|xn--[a-z0-9]{1,59})'              # or punycode label
                r'(?<!-)'                            # can't end with a dash
                r'\.?'                               # may have a trailing dot
        )
        host_re = '(' + hostname_re + domain_re + tld_re + '|localhost)'

        self.url_re = re.compile(
            r'([a-z0-9.+-]*:?//)?'                                       # scheme is validated separately
            r'(?:[^\s:@/]+(?::[^\s:@/]*)?@)?'                           # user:pass authentication
            r'(?:' + ipv4_re + '|' + ipv6_re + '|' + host_re + ')'
            r'(?::\d{2,5})?'                                            # port
            r'(?:[/?#][^\s]*)?',                                        # resource path
            re.IGNORECASE
        )
        return self.url_re
  
  
  def init_patters(self):
      return {
          "DATE_NUM" : "\d{2}[- /.]\d{2}[- /.]\d{,4}",
          "DATE_LONG" : "(\d{1,2}[^\w]{,2}(januari|februari|maart|april|mei|juni|juli|augustus"\
              "|september|october|november|december)([- /.]{,2}(\d{4}|\d{2})){,1})"\
              "(?P<n>\D)(?![^<]*>)",
          "DATE_SHORT" : "(\d{1,2}[^\w]{,2}(jan|feb|mrt|apr|mei|jun|jul|aug|sep|okt|nov|dec)"\
              "([- /.]{,2}(\d{4}|\d{2})){,1})(?P<n>\D)(?![^<]*>)",  
          "TIME" : "(\d{1,2})[.:](\d{1,2})?([ ]?(am|pm|AM|PM))?",
          "POSTAL_CODE" : r"\d{2}[- /.]\d{2}[- /.]\d{,4}",
          "DIGIT" : r"\d",
          "IP": self.init_ip_pattern(),
          "EMAIL" : "(([a-zA-Z0-9_+]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?))(?![^<]*>)",
          "URL" :  "https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+" # self.init_url_pattern()          
    }  
  
  
  def csv_to_list(self, filename, minimum_length=0):
    with open(filename, encoding='latin') as f:
        lst = [line.rstrip() for line in f]
    lst = list(dict.fromkeys(lst))
    if minimum_length > 0:
        lst = list(filter(lambda item: len(item) > minimum_length, lst))
    return lst    
  
  
  def set_key_words(self, word_to_filter, file_name, minimum_length):
      for naam in self.csv_to_list("datasets" + p.sep + file_name, minimum_length):
        wild_card = '<' + word_to_filter +'>'          
        if word_to_filter in ["STREET", "PLACE"]:
            for c in ['.', ',', ' ', ':', ';', '?', '!']:
                self.keyword_processor_case_insensitive.add_keyword(naam + c, wild_card + c)
        elif word_to_filter in ["NAME", "LASTNAME"]:        
            self.keyword_processor_case_sensitive.add_keyword(naam, wild_card)                
        else:
            self.keyword_processor_case_insensitive.add_keyword(naam, wild_card)
                            
  
  def initialize_key_word_processor(self):        
    list_key_words = {
                        "STREET": { "file_name" : "streets.csv", "minimum_length" : 5},
                        "PLACE": { "file_name" : "places.csv", "minimum_length" : 5},                        
                        "NAME": { "file_name" : "firstnames.csv", "minimum_length" : 0},                                              
                        "LASTNAME": { "file_name" : "lastnames.csv", "minimum_length" : 0},                                              
                        "DISEASE": { "file_name" : "diseases.csv", "minimum_length" : 0},                                              
                        "MEDICINE": { "file_name" : "medicines.csv", "minimum_length" : 0},                                              
                        "NATIONALITIES": { "file_name" : "nationalities.csv", "minimum_length" : 0}
                     }
    
    list_key_words_result = []
    list_of_keys = list(list_key_words.keys())               
    for word_to_filter in self.list_words_to_filter:
        if word_to_filter in list_of_keys:   
            file_name = list_key_words[word_to_filter]['file_name']
            minimum_length = list_key_words[word_to_filter]['minimum_length']                   
            list_key_words_result.append(word_to_filter)
            self.set_key_words(word_to_filter, file_name, minimum_length)
            
    return list_key_words_result    
     

  def replace_characters_by_wild(self, start_index, end_index):   
      self.text_email = self.text_email[:start_index] + self.wildcard + self.text_email[end_index:]
   
  
  def censure_key_words(self, list_indexes): 
      for index in list_indexes:
          self.contains_sensitive_data = True
          value_to_replace = self.text_email[index[1]:index[2]]
          self.text_email = self.text_email.replace(value_to_replace, self.wildcard * len(value_to_replace))          
     
    
  def censure_sensitive_data(self):      
      list_of_patterns = list(self.dict_patterns.keys())       
      
      for word_to_filter in self.list_words_to_filter:
          
          if word_to_filter in list_of_patterns:
              pattern = self.dict_patterns[word_to_filter]
              
              if re.search(pattern, self.text_email) is not None: 
                  self.contains_sensitive_data = True    
                               
                  for catch in re.finditer(pattern, self.text_email):
                    current_index = catch.span()         
                    # self.replace_characters_by_wild(current_index[0], current_index[1])                    
                    value_to_replace = self.text_email[current_index[0]:current_index[1]]
                    self.text_email = self.text_email.replace(value_to_replace, self.wildcard * len(value_to_replace))

      return self.text_email  


  def filter(self) -> tuple:     
      # 1. censure key words    
      self.censure_key_words(self.keyword_processor_case_insensitive.extract_keywords(self.text_email, span_info=True))    
      self.censure_key_words(self.keyword_processor_case_sensitive.extract_keywords(self.text_email, span_info=True))    
        
      # 2. censure data
      self.censure_sensitive_data()
        
      return self.contains_sensitive_data, self.text_email.strip()


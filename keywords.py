class keywordsDict:
    def __init__(self):
        """ contains the vocabulary database for each job type with two dimensions: 
        hard skill and soft skills (communication and networking)
        
        keywods: integrated result in a dictionary
        """
        
        de_key1 = ['design','product','market','media','visual','graphic','excel','photoshop',
                   'adobe','ux','ui','autocad','figma','powerpoint', 'java', 'xml', 'css']
        de_key2 = ['team','creative','collaborative','detail','responsible','innovative',
                   'international','english','chinese','mandarin', 'communication', 'user','customer','client']

        da_key1 = ['analysis','science','systems','computer','technology','software','sql','programming',
                  'python','java','web','c','research','bachelors','model','statistics','machine','excel',
                  'visualization', 'tableau','microsoft','quantitative','mathematics','linux','university',
                  'r','javascript','html','vba','vlookup','media', 'data']
        da_key2 = ['english', 'users', 'problemsolving', 'multitask', 'collaborator','multidisciplinary',
                  'vigilant','vision']

        bm_key1 = ['market','fund','invest','business','risk','oredb','finance','trade','trend','service',
                  'sales','strategy','portfolio','revenue','bank','excel','ms','sharepoint','powerpoint','word']
        bm_key2 = ['concise','challenging','team','collaborative','leadership','voluntary','independent',
                  'passion','negotiate','responsible','cantonese','english','mandarin']

        con_key1 = ['autocad','python','matlab','mba','cpa','cma','vba','word','powerpoint','market',
                   'digital','model','statistics','portfolio','economics','finance','venture','miscellaneous']
        con_key2 = ['result','passion','pressure','positive','multiple','proactive','curiosity','creative',
                   'ambitious','logical','energetic','outgoing','reasoning','cantonese','english','mandarin']

        fa_key1 = ['accountancy','analysis','assurance','audit','budget','bank','cfa','cpa','finance','market',
                  'portfolio','powerpoint','sales','risk','securities','statistics','treasury','trade']
        fa_key2 = ['active','effective','experience','initiative','innovative','insightful','logical','mindset',
                  'positive','pressure','responsible','solving','intelligence','detail','cantonese','english','mandarin']

        eng_key1 = ['program','production','machinery','excel','word','model','software','hadoop','spark',
                   'azure','aws','python','gcp','maxos','android','outlook','browser','g4','app','code',
                   'wr2','polyglots','ee','javascript','redux','rpa']
        eng_key2 = ['responsible','solve','team','manage','independent','troubleshooting','efficient',
                   'critical','confident','selfmotivated','interact','english','cantonese','mandarin']
        
        de_keyword_dict={'Hard Skills': de_key1, 'Soft Skills: communication+networking': de_key2}
        da_keyword_dict={'Hard Skills': da_key1, 'Soft Skills: communication+networking': da_key2}
        bm_keyword_dict={'Hard Skills': bm_key1, 'Soft Skills: communication+networking': bm_key2}
        con_keyword_dict={'Hard Skills': con_key1, 'Soft Skills: communication+networking': con_key2}
        fa_keyword_dict={'Hard Skills': fa_key1, 'Soft Skills: communication+networking': fa_key2}
        eng_keyword_dict={'Hard Skills': eng_key1, 'Soft Skills: communication+networking': eng_key2}
        
        keyword_list={'Designer': de_keyword_dict, 'DataAnalyst':da_keyword_dict,
             'BusinessManager':bm_keyword_dict,'Consultancy':con_keyword_dict,
             'FinancialAnalyst':fa_keyword_dict, 'Engineer':eng_keyword_dict}
        
        self.keywords = keyword_list
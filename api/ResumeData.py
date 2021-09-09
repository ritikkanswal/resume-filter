# Import required libraries
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

import textract
import re
import string
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

def GetResumeDetails(filename):
    # Open pdf file
    output_string = StringIO()
    with open(filename, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    text=output_string.getvalue()

    # Convert all strings to lowercase
    text = text.lower()

    # Remove numbers
    text = re.sub(r'\d+','',text)

    # Remove punctuation
    text = text.translate(str.maketrans('','',string.punctuation))

    # Create dictionary with industrial and system engineering key terms by area
    terms = {'Competitive Programming':['codechef','codeforces','hackerearth','spoj'
                                        'hackerank','kickstart','icpc','leetcode'],      
        'Cloud Service':['automation','aws','ec2','s3'],
        'Web Development':['html','css','javascript']}


    # Initializie score counters for each area
    quality = 0
    operations = 0
    supplychain = 0
    project = 0
    data = 0
    healthcare = 0

    scores = []
    res={'Competitive Programming':0,'Cloud Service':0,'Web Development':0}
    # Obtain the scores for each area
    for area in terms.keys():
            
        if area == 'Competitive Programming':
            for word in terms[area]:
                if word in text:
                    quality +=1
            scores.append(quality)
            res['Competitive Programming']+=quality
            
        elif area == 'Cloud Service':
            for word in terms[area]:
                if word in text:
                    operations +=1
            scores.append(operations)
            res['Cloud Service']+=operations
            
        elif area == 'Web Development':
            for word in terms[area]:
                if word in text:
                    supplychain +=1
            scores.append(supplychain)
            res['Web Development']+=supplychain
    return res
# print(GetResumeDetails("r.pdf"))
# # Create a data frame with the scores summary
# summary = pd.DataFrame(scores,index=terms.keys(),columns=['score']).sort_values(by='score',ascending=False)
# summary

# # Create pie chart visualization
# pie = plt.figure(figsize=(10,10))
# plt.pie(summary['score'], labels=summary.index, explode = (0.1,0,0), autopct='%1.0f%%',shadow=True,startangle=90)
# plt.title('Resume Filtering')
# plt.axis('equal')
# plt.show()

# # Save pie chart as a .png file
# pie.savefig('resume_screening_results.png')

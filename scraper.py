import requests
from bs4 import BeautifulSoup



class Job:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc
    
  def __str__(self):
    return f'Job title: {self.name} + Description: {self.desc}'

def formatTxt(text,tag):
  openTag = f'<{tag}>'
  closeTag = f'</{tag}>'
  return str(text).replace(openTag,'').replace(closeTag,'')

listOfJobs = []

for x in range (1,15): 
    print('Page',x)
    URL = "https://www.jobindex.dk/jobsoegning?page=2&q=python".replace("NUMBER",str(x))
    page = requests.get(URL)
    #print(page)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="result_list_box")

    job_elements = results.find_all("div", class_="jobsearch-result")

    for job_element in job_elements:
        title_element = formatTxt(job_element.find("b"),'b')
        desc_element = ""
        for tag in job_element.findAll("p"):
          desc_element += formatTxt(tag,'p') + "\n"

        tmpJob = Job(title_element,desc_element)
        listOfJobs.append(tmpJob)
        print(tmpJob)
        print("\n __________________________________________________________________________________")
        
        
        
    print(len(job_elements))
#python_jobs = results.find_all(
  #  "h2", string=lambda text: "python" in text.lower()
#)
#python_job_elements = [
 #   h2_element.parent.parent.parent for h2_element in python_jobs
#]
#print(listOfJobs)
import requests
import bs4
 

#varables

Name = []
Time = []
lecturer = []
sections_num = []


#get url
url= "https://www.coursat.org/subject/python"
page = requests.get(url).content


# create soup object
soup = bs4.BeautifulSoup(page , "lxml")

# get element we need
course_name = soup.find_all ('div', {'class': 'course-title'})


lecturer_name = soup.find_all ('div', {'class': 'course-instructor'})
#print (lecturer_name)

duration = soup.find_all('div', {"class": "","title":"مدة الكورس"})
#print (duration)


sec_num =  soup.find_all ('div', {'class': '',"title": "عدد الدروس" })
#print (sec_num)


#extract element text
for i in range(len(course_name)):
    Name.append(course_name[i].text.strip())

    Time.append(duration[i].text.strip())
    sections_num.append(sec_num[i].text.strip())
    lecturer.append(lecturer_name[i].text.strip())

print(Name)
print(Time)
print(sections_num)
print(lecturer)

response = requests.get("https://nanoreview.net/en/cpu-list/laptop-chips-rating")
    soup = BeautifulSoup(response.text,'html.parser')
    #print(soup)
    m=soup.find('tbody').find_all('a')
    for a in m:
        a_text= a.get_text()
        print(a_text)
except Exception as e:
    print(e)
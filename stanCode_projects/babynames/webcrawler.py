"""
File: webcrawler.py
Name:
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=header)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all('tbody')
        # print(tags)
        male_num = 0
        female_num = 0

        for tag in tags:
            text = tag.text
            text = text.strip()
            text = text.split()   # text becomes a list
            # print(text)
            for i in range(len(text)):
                if text[i] == 'Source:':
                    break
                elif i % 5 == 2:   # i == 2, 7, 12, 17, 22...
                    # text[i] = text[i].replace(",", "")
                    split_text = text[i].split(',')
                    # text[i] = "".join(text[i].split(','))
                    join_text = "".join(split_text)      # join_text is a string
                    male_num += int(join_text)
                elif i % 5 == 4:   # i == 4, 9, 14, 19, 24...
                    # text[i] = text[i].replace(",", "")
                    split_text = text[i].split(',')
                    join_text = "".join(split_text)
                    female_num += int(join_text)
        print('Male Number:', male_num)
        print('Female Number:', female_num)


if __name__ == '__main__':
    main()

# coding=utf-8
import sys
import json
import requests
from lxml import html


def solve(nickname) :
    # ����
    url = "https://codeforces.com/profile/" + nickname
    response = requests.get(url) 

    # ������سɹ�
    if response.status_code == 200 :
        try:
            # ��ȡ���� 
            content = html.fromstring(response.content)
            rating = content.xpath('//div[@class="info"]/ul/li[1]/span/text()')
            rank = content.xpath('//div[@class="user-rank"]/span/text()')

            #������rankʱ
            if rank[0] == "Unrated " :

                people = {
                    "handle" : nickname
                }

                output = json.dumps(people) 
                print(output, file=sys.stdout)
                sys.exit(0)
            elif rating and rank :

                rank_t = rank[0] 
                rank_t = rank_t.rstrip(" ")

                people = {
                    "handle": nickname ,"rating": rating[0],"rank": rank_t
                }

                output = json.dumps(people)
                print(output, file=sys.stdout)
                sys.exit(0)
            # �û�������ʱ 
            else:
                print("no such handle", file=sys.stderr)
                sys.exit(1)
        except IndexError:
            print("no such handle", file=sys.stderr)
            sys.exit(1)

def main():
    # print("please input one nickname:")
    nickname = sys.stdin.readline().strip()
    solve(nickname) 
    
if __name__ == "__main__" :
    main() 
# coding=utf-8 
import sys 
import json 
import requests 
from fake_useragent import UserAgent
import random 


def solve(nickname):
    # ģ��ͻ��˷�����Ϣ 
    try:
        imfo_t = "user.info" 
        ex_url = f"https://codeforces.com/api/{imfo_t}"

        ex_user_agent = UserAgent()
        ex_header = {"User-Agent": ex_user_agent.random} 
        # print(ex_user_agent.random)

        ex_par = {"handles": nickname} 
        response = requests.get(ex_url, params=ex_par , headers=ex_header)
        
        # ������� 
        if response.status_code != 200 :
            print("no such handle") 
        else : 
            # ���ݡ�status"���������� 
            data = json.loads(response.text) 
            if data["status"] == "FAILED": 
                print("no such handle") 
                sys.exit(1) 
            elif data["result"][0]["contribution"] == 0 :
                people = {
                    "handle" : nickname[0] 
                }
                print(json.dumps(people) , file= sys.stdout) 
                sys.exit(0)
            elif data["result"][0]["contribution"] != 0 :
                people = {
                    "handle" : nickname[0] , 
                    "rating" : data["result"][0]["rating"],
                    "rank" : data["result"][0]["rank"] 
                }
                print(json.dumps(people) , file= sys.stdout) 
                sys.exit(0)

    except IndexError: #����Խ���ʱ�򲶻�
        print("no such handle", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as e: #requests����ı��� 
        print("An error occurred: {e}" ,file = sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e: #json�����ı��� 
        print("An error occurred while parsing JSON: {e}",file = sys.stderr)
        sys.exit(1)
    except Exception as e: #�����ı�������������� 
        print("An error occurred: {e}",file = sys.stderr)
        sys.exit(1)
    return 0 

def main():
    nickname = sys.stdin.readline().split() 
    solve(nickname) 

if __name__ == "__main__" :
    main() 
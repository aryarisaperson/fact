import requests
url="https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"



def get_facts():
    response=requests.get(url)
    fact=response.json()
    
    text=fact["text"]


    return text

def main():
    while True:
        text=get_facts()
        user=input("Do you want to know some random or useless stuff?(y/n)")
        if user=="y":
            print(f"Did you know that {text}? \n\n\n")
        else:
            print("\n\n\nAwwwwwww.")
            break


if __name__=="__main__":
    main()
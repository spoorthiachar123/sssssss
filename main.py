import requests
from bs4 import BeautifulSoup

cookies = {
    'g_a': 'KPWuAU+11FLgF87/kf5dSQRfWFlTOyLxWGhLZQyMTbWeDYogFoXh0SmRdfbskltj',
    'g_b': '8w0RuVZuNIgq8jo+Qq+6QI3lVIFUHkxmTJWdatQAL8meQFhtNh3JvoMcDi1dE5CpqFntSFdkeg/lmsrA8g8f/I3QwE8lehXQReQddB/LEQo=',
    'g_c': 'KrHdbuAi7zTKyrfXKV6ud4hqbN/b9rvW6VbPQ2WksX5fzXP6QcpL+wnh10XMNWydRepwNod8M0gAdhDj7hp5Qtf85H9NIPcWs9sobIx8ENzN3V0Hrerx9LGmI7ICQ6sH48q9bwNE0fpTWLAU6eUZTeXohFuMz75PSxRxtjnx5Xt0nw2xu1OabDN1cBt8qKFPUpzgIJ/W+j0OGonYWQEHt/DWAgdf43ilearoIuK0aDkzlpsO3jdCeOQvRoefIxQNp6qejZPQrOFry3cbmYPIXnKgDJM9ViPhVcfd9Fm+NdyPiPVhiVW+6peUj3dvJWh/M7QALz2auENgOq1osUdyQOIsX0FL3AchI0q1vF2KzAn5P+uuBFg5uF/bwecQvWYhm058h4dbYq7ROai7cMlSNvVPyxhsI4FVwggt0NFsuBUJV/TqZs5zCqN+qh7KTMzwxDUOPMdpT85NqQXzzs4+zNB8ECD0v2cZza9KOX/U14zoSVXbQNVsgvv19E5rjoO/RzxzF8/tmahmQZaz9E7OPhEoo/rwN5bTrV6A/GbzlDFVOSuC4r9fLBcDGFk7ZQrI1tXtQxdQoYuKzxMhNTWqToDHvb620mGAITWJ/2/ao7T5+bK8GLPXy/we0NvRy+yC3SznQSsDKbKHvZIVxCHTLjozFTVewSS4MQJwEPDKcsLZS07MB16HrOW2S4eKw0ne01pXlAudEUrwMR70/OISvNnZb0zzNPYL4bBfIma3NwDO2kTM0l10o5J6xSCGuS3v+MDj7wdpNmrWnYB+vIzz6gYeZN6jxCmHteUM+A5w7xfthQjBSxBlVH4B4keRNNDvrVN7TY2vM3mBVKaHxrSoEr0jNORW0a+Yv11O+geUMbtnbjAb8XtN/NEckld6gTyRO7nWdcdB42oqsiZbDr0D7Q8PEoafDZP1fMjEg3BdHCEKyOXkUw3ASmgtKnGW/LpHjBaNTC+wAq3jCA9FfcjeRsGiXE9qXWStOtCr3vD+pZlaJvC/g0lq18q12qa/w6vRsRLSSTaBOtvEnNHRlc/zrvJTbjWQYz/HeewqR3KqV5cx1dWDxotEQY+KcCmngGRdddo1nRS8E+3d5jKlmM4Ew3BSuLUFX5Wm7hFcjA5lcQoUG09fL7c0FtcvtQZjj02VJE/bevJgtdP0VZfXT5AIuCx2EAP1Ob3+Fw47okanRZHVtUuwBMkq6wRpQrhrTOUZ7qfaGG2P1VAPLVPywtjEnHgcL7oJWTKz0D4yaw81gE1SehNYDqjqKaM7ar3Dnh6WhnUBB2Hg1Aaof2KBNYbnN4ijsf5plItCoXW25qhkSkG0uemlKQvIc/2lfQqRWjuN',
}

headers = {
    'authority': 'onlinecourses.nptel.ac.in',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    # 'cookie': 'g_a=KPWuAU+11FLgF87/kf5dSQRfWFlTOyLxWGhLZQyMTbWeDYogFoXh0SmRdfbskltj; g_b=8w0RuVZuNIgq8jo+Qq+6QI3lVIFUHkxmTJWdatQAL8meQFhtNh3JvoMcDi1dE5CpqFntSFdkeg/lmsrA8g8f/I3QwE8lehXQReQddB/LEQo=; g_c=KrHdbuAi7zTKyrfXKV6ud4hqbN/b9rvW6VbPQ2WksX5fzXP6QcpL+wnh10XMNWydRepwNod8M0gAdhDj7hp5Qtf85H9NIPcWs9sobIx8ENzN3V0Hrerx9LGmI7ICQ6sH48q9bwNE0fpTWLAU6eUZTeXohFuMz75PSxRxtjnx5Xt0nw2xu1OabDN1cBt8qKFPUpzgIJ/W+j0OGonYWQEHt/DWAgdf43ilearoIuK0aDkzlpsO3jdCeOQvRoefIxQNp6qejZPQrOFry3cbmYPIXnKgDJM9ViPhVcfd9Fm+NdyPiPVhiVW+6peUj3dvJWh/M7QALz2auENgOq1osUdyQOIsX0FL3AchI0q1vF2KzAn5P+uuBFg5uF/bwecQvWYhm058h4dbYq7ROai7cMlSNvVPyxhsI4FVwggt0NFsuBUJV/TqZs5zCqN+qh7KTMzwxDUOPMdpT85NqQXzzs4+zNB8ECD0v2cZza9KOX/U14zoSVXbQNVsgvv19E5rjoO/RzxzF8/tmahmQZaz9E7OPhEoo/rwN5bTrV6A/GbzlDFVOSuC4r9fLBcDGFk7ZQrI1tXtQxdQoYuKzxMhNTWqToDHvb620mGAITWJ/2/ao7T5+bK8GLPXy/we0NvRy+yC3SznQSsDKbKHvZIVxCHTLjozFTVewSS4MQJwEPDKcsLZS07MB16HrOW2S4eKw0ne01pXlAudEUrwMR70/OISvNnZb0zzNPYL4bBfIma3NwDO2kTM0l10o5J6xSCGuS3v+MDj7wdpNmrWnYB+vIzz6gYeZN6jxCmHteUM+A5w7xfthQjBSxBlVH4B4keRNNDvrVN7TY2vM3mBVKaHxrSoEr0jNORW0a+Yv11O+geUMbtnbjAb8XtN/NEckld6gTyRO7nWdcdB42oqsiZbDr0D7Q8PEoafDZP1fMjEg3BdHCEKyOXkUw3ASmgtKnGW/LpHjBaNTC+wAq3jCA9FfcjeRsGiXE9qXWStOtCr3vD+pZlaJvC/g0lq18q12qa/w6vRsRLSSTaBOtvEnNHRlc/zrvJTbjWQYz/HeewqR3KqV5cx1dWDxotEQY+KcCmngGRdddo1nRS8E+3d5jKlmM4Ew3BSuLUFX5Wm7hFcjA5lcQoUG09fL7c0FtcvtQZjj02VJE/bevJgtdP0VZfXT5AIuCx2EAP1Ob3+Fw47okanRZHVtUuwBMkq6wRpQrhrTOUZ7qfaGG2P1VAPLVPywtjEnHgcL7oJWTKz0D4yaw81gE1SehNYDqjqKaM7ar3Dnh6WhnUBB2Hg1Aaof2KBNYbnN4ijsf5plItCoXW25qhkSkG0uemlKQvIc/2lfQqRWjuN',
    'referer': 'https://onlinecourses.nptel.ac.in/noc23_cs18/unit?unit=122&lesson=127',
    'sec-ch-ua': '"Brave";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

params = {
    'name': '147',
}

response = requests.get(
    'https://onlinecourses.nptel.ac.in/noc23_cs18/assessment',
    params=params,
    cookies=cookies,
    headers=headers,
)

soup = BeautifulSoup(response.content,'html.parser')

# Find all div elements on the page
div_elements = soup.find_all('div',{'class':'qt-mc-question qt-embedded'})

# for div in div_elements:
#     print(div.text)

with open ('out.txt','w',encoding='utf-8') as f:

    # Loop through the div elements and extract their contents
    for div in div_elements:
        

        question_div = div.find('div',{'class':'qt-question'})
        f.write("\n_______________Question_____________________\n")
        f.write(question_div.text)
        f.write("\n____________________________________________\n")
        choices_div = div.find('div',{'class':'qt-choices'})
        f.write(choices_div.text)

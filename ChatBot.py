from nltk.chat.util import Chat, reflections
pairs=[['My name is (.*)',['Hi %1']],
       ['(.*) is your name?',['My name is JARVIS The Robot!']],
       ['(Hi|Hello|Heyy|hey)',['Hey there','Hi','Hellooo','Hello, nice to meet you']],
       ['(.*) created you?',['Abdul Fatir Sir did']],
       ['How is the weather in (.*)',['The weather is Good in %1']],
       ['(.*) help (.*)',['I can help you']]]
chat=Chat(pairs, reflections)
chat.converse()

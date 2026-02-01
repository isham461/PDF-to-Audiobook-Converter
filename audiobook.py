import PyPDF2 as pf
import pyttsx3 as pt
def texttovoice(filename):
    try:
        with open(filename,"rb")  as book:
            reader=pf.PdfReader(book)
            totalpages=len(reader.pages)
            full_text=""
            speaker=pt.init()
            speaker.setProperty("rate",150)
            for page_num in range(totalpages):
                page=reader.pages[page_num]
                text=page.extract_text()
                if text:
                    full_text=full_text+text+" "
            choice=int(input("1.Listen to audio\n2.Listen and save\n3.Save audio\nPlease choose any of these option (1/2/3) : "))
            if choice==1:
                speaker.say(full_text)
                speaker.runAndWait()
            elif choice==2:
                aud=input("Enter file name for audio to be saved (with .wav extension) : ")
                speaker.save_to_file(full_text,aud)
                speaker.runAndWait()
                print("Audio saved successfully...")
                del speaker
                speaker=pt.init()
                speaker.say(full_text)
                speaker.runAndWait()
                
            elif choice==3:
                speaker.save_to_file(full_text,aud)
                speaker.runAndWait()
                print("Audio saved successfully...")
            else:
                print("Invalid Option")              
    except FileNotFoundError:
        print("File not found")
    except KeyboardInterrupt:
        print("Paused!!!")
    except:
        print("Error Occured")
filename=input("Enter the file name(with .pdf extension) : ")
texttovoice(filename)

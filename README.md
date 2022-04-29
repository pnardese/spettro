Plotta lo spettro di una sorgente luminosa misurata con spotread e uno spettrofotometro X-Rite Colormunki.
Di seguito un esempio di immagine prodotta di una sorgente LED.

![LED](https://user-images.githubusercontent.com/16850090/165939150-72d35a68-0bfc-4ce9-890a-66b51755c6de.png)

opzioni spotread:

ambient light spectrum\n
spotread -v -s -H -a -T "file.sp"

reflectance spectrum
spotread -v -s -H -T "file_refl.sp"

transmission spectrum
spotread -v -s -H -t -T "file_trans.sp"

emission spectrum
spotread -v -s -H -e -T "file_emiss.sp"

flash emission spectrum
spotread -v -s -H -f -T "file_flash.sp"


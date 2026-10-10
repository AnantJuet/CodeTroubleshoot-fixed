Bugs I found and fixed

Node app (book catalog)

1. Search route (src/routes/books.js)
/search was written after /:id, so Express took "search" as a book id and
the search endpoint never worked. I moved /search above /:id.

2. Category filter (src/repositories/bookRepository.js)
The query had "category != ?", so picking Science showed everything except
Science. Changed it to "=".

3. Stock decrease (src/services/stockService.js)
When the adjustment was negative, the code used Math.abs() so the minus
button was adding stock instead of removing it. Now it is just
quantity + adjustment, and the "Insufficient stock" check works.

4. Edit book (src/services/bookService.js)
updateBook took (publishedYear, price) but the controller sends
(price, published_year). Price and year got mixed up on every edit. I put
the parameters in the same order as the controller.

5. Copies in stock (src/repositories/statsRepository.js)
It only counted books with quantity > 1, so books with 1 copy were left out.
Changed to SUM(quantity).

6. Search box (frontend/js/app.js)
The search used the value from the previous keystroke, so results were
always one letter behind. It now uses the current text.


Python app (handwriting OCR)

1. Download was empty (app/utils/files.py)
read_result opened the file with "w+", which wipes the file before reading.
Changed it to "r".

2. Wrong image sent to OCR (app/services/pipeline.py, app/recognition/ocr.py)
prepare_for_ocr was called with the arguments the wrong way round, so the
original colour image went to Tesseract and not the processed one. I made
it take only the processed image and flip it to black text on white, since
Tesseract reads that better.

3. Image stretched (app/preprocessing/image_ops.py)
Every image was forced to 800x600, which squashed wide and tall images and
made the text unreadable. Now it resizes keeping the aspect ratio.

4. Only one line read (app/recognition/ocr.py)
The config had --psm 7, which is single line mode. Multi line notes lost
text. Changed to --psm 6.

How I tested
After the fixes all four sample images in python/samples give the right
text, for example "The quick brown fox jumps". For the Node app I checked
search, category filter, the stock buttons, edit and the stats on the page.

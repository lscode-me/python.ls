# Data Transfer Encoding - Quiz

Test your knowledge on "Data Transfer Encoding".

---

## Question 1: Base64 Purpose

What is Base64 used for?

A) Hashing

B) Data encryption

C) Representing binary data as text

D) Data compression

---

## Question 2: Base64 Characters

How many characters does standard Base64 use?

A) 256

B) 32

C) 128

D) 64

---

## Question 3: Base64 Size

How much does Base64 encoding increase data size?

A) ~50%

B) ~10%

C) ~33%

D) ~100%

---

## Question 4: Base64 Padding

What does the `=` symbol mean at the end of a Base64 string?

A) Encoding error

B) End of data

C) Separator

D) Padding for alignment

---

## Question 5: URL Encoding

How is a space encoded in URLs?

A) `\ `

B) `_`

C) %20 or +

D) `%10`

---

## Question 6: URL-safe Base64

What characters are used in URL-safe Base64 instead of `+/`?

A) -_

B) `$.`

C) `~!`

D) `*&`

---

## Question 7: Python base64

How do you encode a string to Base64 in Python?

A) base64.b64encode("text".encode())

B) `base64.encode("text")`

C) `"text".to_base64()`

D) `encode64("text")`

---

## Question 8: urlencode

What Python function encodes URL parameters?

A) `params.to_url()`

B) urllib.parse.urlencode(params)

C) `encode_url(params)`

D) `url.encode(params)`

---

## Question 9: MIME Type JSON

What is the MIME type for JSON?

A) `json/text`

B) `text/json`

C) `data/json`

D) application/json

---

## Question 10: Data URL

How does a Data URL for a PNG image start?

A) `base64:image/png;`

B) `png:data;base64,`

C) data:image/png;base64,

D) `image:data/png;`

---

## Question 11: Content-Type charset

How do you specify UTF-8 in Content-Type?

A) `text/html; encoding=utf-8`

B) `text/html+utf-8`

C) `text/html; utf-8`

D) text/html; charset=utf-8

---

## Question 12: Percent Encoding

How do you encode the `&` character in URLs?

A) `%27`

B) %26

C) `%28`

D) `%25`

---

## Question 13: JWT

In what format are JWT token parts encoded?

A) Hex

B) ASCII85

C) Base32

D) Base64 URL-safe

---

## Question 14: multipart/form-data

What is multipart/form-data used for?

A) Uploading files via forms

B) Text forms only

C) JSON data

D) Form compression

---

## Question 15: Encoding Security

Is Base64 encryption?

A) No, it's only encoding, data easily decodable

B) Yes, it's secure encryption

C) Yes, if you use a password

D) Depends on the data

---

## Question 16: Base32

What characters does Base32 use?

A) All ASCII characters

B) A-Z and 2-7

C) Only letters

D) 0-9 and A-F

---

## Question 17: quote/unquote

What Python functions encode/decode individual strings for URLs?

A) url_encode/url_decode

B) encode/decode

C) quote/unquote

D) escape/unescape

---

## Question 18: Content-Disposition inline

What does `Content-Disposition: inline` mean?

A) Compress file

B) Download file

C) Delete file

D) Display file in browser

---

## Question 19: multipart boundary

What is the boundary used for in multipart/form-data?

A) Separating form parts

B) Encryption

C) Data compression

D) Size calculation

---

## Question 20: parse_qs

What does `urllib.parse.parse_qs()` do?

A) Encodes URL

B) Creates query string from dictionary

C) Decodes Base64

D) Parses query string into dictionary

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Base64 transforms binary data into ASCII text for transmission. |
| 2 | C | Base64 uses 64 characters: A-Z, a-z, 0-9, +, /. |
| 3 | D | 3 bytes → 4 characters, approximately 33% increase. |
| 4 | A | `=` — padding to make length multiple of 4. |
| 5 | C | Space → `%20` or `+` (in query string). |
| 6 | B | URL-safe Base64 uses `-` and `_` instead of `+` and `/`. |
| 7 | A | `b64encode` takes bytes, needs `.encode()`. |
| 8 | B | `urllib.parse.urlencode()` encodes dictionary to query string. |
| 9 | D | Correct MIME type: `application/json`. |
| 10 | A | Data URL: `data:mime/type;base64,<data>`. |
| 11 | D | Parameter `charset=utf-8` specifies encoding. |
| 12 | A | `&` = `%26` (26 hex = 38 dec = ASCII `&`). |
| 13 | C | JWT uses Base64 URL-safe without padding. |
| 14 | A | multipart/form-data used for file uploads in HTML forms. |
| 15 | B | Base64 — encoding, not encryption. Anyone can decode. |
| 16 | D | Base32 uses A-Z (26) + 2-7 (6) = 32 characters. |
| 17 | B | `quote()` encodes string, `unquote()` decodes. |
| 18 | D | `inline` — display in browser, `attachment` — download. |
| 19 | C | boundary separates different form parts (fields, files). |
| 20 | B | `parse_qs()` parses query string into dictionary of lists. |

---

## Scoring Guide

| Result | Rating | Recommendations |
|--------|--------|----------------|
| **17-20 correct (85-100%)** | 🏆 Excellent! | You master data encoding! |
| **14-16 correct (70-84%)** | ✅ Good | Review URL encoding and MIME types. |
| **10-13 correct (50-69%)** | ⚠️ Satisfactory | Re-read Base64 section. |
| **Less than 10 correct (<50%)** | 📚 Needs Review | Recommended to re-read the lecture. |

---

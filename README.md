# Html2Latex Convertor
HTML to LaTeX convertor implemented using Lex and Yacc made for assignment of course COL701 at IIT Delhi

# Demo

```sh
$ pip install -r requirements.txt
$ bash demo.sh
```

The output pdf will be in `examples/sample1.pdf`

# Details

In this assignment the main objective is to convert a HTML document to an equivalent LaTeX document. In pursuance of this objective, have written a HTML to LaTeX parser from scratch. The exact problem statement is given in [problem_statement.pdf](problem_statement.pdf)

The features(tags) of HTML which we all needed to consider are:

* head
* body
* title
* a, href
* font: size
* center
* br
* p
* h1, h2, h3, h4
* ul, li, ol, ul, dl, dt, dd
* div
* u, b, i, em, tt, strong, small,
* sub, sup
* img: src, width, height, figure, figcaption
* table, caption, th, tr, td

For more details refer to [report.pdf](report.pdf)




# Documentation for Quickmark

> Markdown is a lightweight markup language for creating formatted text using a plain-text editor.
> *- Wikipedia*

In short, Markdown is a way to quickly write documents that will render properly across machines (using predefined rules). Quickmark currently supports Github-flavoured Markdown (GFM).

## Github-flavoured Markdown

### 1. Headings

You have 6 different sizes of headings (according to `<h1>` to `<h6>`):

```markdown

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

```

### 2. Paragraphs

In order to write normal text (e.g. no special sizing), you simply write text normally, without using any special characters to indicate so:

```markdown

I am writing some text, this is a Paragraph in Markdown.

```

### 3. Text Styling

As you may have noticed, you can style your text a bit, when needed. Your options are:

1. Italic
2. Bold
3. (inline) Code
4. Strikethrough
5. Quote

```markdown

*this is italic*
**this is bold**
`this_is_code();`
~~this is strikethrough~~
> This is a quote

```

### 4. Special Text

You can also insert links, and images:

```markdown

This is text [link](https://my_url.com/) more text

This is an image:
![Image](https://link_to_image.com/image.png)
```

### 5. Special Blocks

You can insert special blocks throughout your document, such as lists, code blocks and tables.

To make a code block:

<code>
``` <br>
This is a code block <br>
some_code(1, 2, 3); <br>
```
</code>

to get styling on your code, after the first <code>```</code>, write the name of your language. For example:

<code>
```python <br>
def hello(): <br>
    print("Hello World!") <br>
```
</code>

will render as:

```python
def hello(): 
    print("Hello World!") 
```

To make a list:

```markdown

1. This is a numbered list
2. ...

- This is a bulleted list
- ...
```

And finally, to make a table you need to "draw" the table using characters like `|` and `-`.

```markdown

| Name       | Price (USD) |
|------------|-------------|
| Bitcoin    | $36,011.92  |
| Ethereum   | $2,552.78   |
| Monero     | $265.70     |
| Cardano    | $1.58       |

```

will render as:

| Name       | Price (USD) |
|------------|-------------|
| Bitcoin    | $36,011.92  |
| Ethereum   | $2,552.78   |
| Monero     | $265.70     |
| Cardano    | $1.58       |

note, you don't actually have to match the lines exactly, so the following table would still render out the same way (but, it would look worse while editing it).

```markdown

| Name|Price (USD)|
|-----|-----------|
| Bitcoin| $36,011.92|
| Ethereum| $2,552.78|
| Monero| $265.70|
| Cardano| $1.58|

```

## Quickmark Features

In core, the main feature of Quickmark is having custom styling, and loading scripts as needed.

To achieve this, using the following syntax to denote to the compiler to load/use something:

```markdown
@[script1, script2, script3, ...,]
@:[your style name/config]
@![additional compile arguments]
```

Insert these statements at the top of your file, before any actual content. Obviously, these won't be rendered into your final output.

Below is an example document, and its HTML output.

```markdown
@[mathjax]
@:[styleconfig1]
@![title My Document]

# Hello World!

Some text `code()` more text.

$$ e^x \geqslant x + 1 $$

```

```html
<!DOCTYPE html>
<html>
    <head>
        <title> My Document </title>
        <style> /* import styleconfig1 */ </style>
        <script src="mathjax.js"></script>

        <!-- Auto inserted by Quickmark -->
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <h1 class="qm-h1"> Hello World! </h1>
        <p class="qm-p"> Some text <code class="qm-code">code()</code> more text. </p>

        <p class="qm-p"> $$ e^x \geqslant x+1 $$
    </body>
</html>
```

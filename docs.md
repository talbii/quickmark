# Documentation/Syntax for Quickmark

*(yes, I do realise this is written in Markdown)*

------------------

Quickmark, is aiming to be a substitute for Markdown - but not to replace it. I have a lot of respect for Markdown's simplicity, and Quickmark is very much based on it.

The main feature I wanted to bring to Quickmark, is customizable styling, without knowledge of HTML/CSS.

## Pre-Document Headers

### Manual Headers

In order to achieve customized styling, before writing your document, you can use setting-headers, which like the name suggests, set specific things. To access said headers, use `@!` (this was chosen in order to not conflict with any possible text).

#### Example File

```quickmark
@!font->text("MyFont")
@!font->code("MyMonospaceFont")
@!text->size(18)
@!code->size(18)
@!heading->size(28)
@!heading->colour(red)
@!margin->vertical(100)
...

@$h My Heading!

Lorem ipsum dolor `some_code(1,2,3)` sit amet consectetur.
```

any text written after a full setting statement (e.g. `@!font->text("MyFont)`) will be treated as a comment, and will not be printed onto your document.

### Themes

Setting **all** of the headers manually can be very annoying, and will defiantly take a long time, let alone a lot of lines. In order to combat this, you can also use a theme, which has packed already all of the styling into one import. In order to use a theme, you

1. Need to make sure the theme is available in the project directory/compiler accessible
2. Make sure the theme is valid, and has correct syntax.
3. Finally, to use a theme write `@theme->"MyTheme"` at the top of your file.

*Note: Using/creating a theme is just a predefined list of headers which have been set in advance. Theme creators may add customizability to their themes, using options. In order to access the options, the user only has to add `[]`, like so: <code> @theme->"MyCustomizableTheme"[*options*]</code>*

Quickmark comes already with 2 predefined themes: `Standard` and `StandardDark`, which have a few options. I encourage you to create themes, since I don't know much about design.

### Creating your own theme

TODO

## Document Headers

As you've noticed in the example before, there also exist a small amount of document headers:

- Heading (`h1`-`h6`) - <code> @$h[*number*] Text</code> (`number` defaults to 1).
- Bold - `**Text**`
- Italics - `*Text*`
- Code - <code> `Text` </code>

*Note: Only the heading requires using a `@` tag*

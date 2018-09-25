# Tutorial

You need to [install](/README.md#installation) **shortcuts** first.

---

This project uses [toml](https://github.com/toml-lang/toml) to describe shortcuts.

A shortcut is a sequence of actions. Every action can receive some input and can produce output.

Let's write a simple shortcut, which asks the name of our user and then prints it back in an alert.

At first, we need to ask our user:

```toml
[[action]]
type = "ask"
question = "What is your name?"
```

You can see above that we created an array item in the `[[action]]`. It will create a Shortcut action which asks our user and returns his answer as an output. Now we can do something with the answer.

Let's save it to a variable.

```toml
[[action]]
type = "set_variable"
name = "name"
```

And now let's print a message for the user:

```toml
[[action]]
type = "show_result"
text = "Hello, {{name}}!"
```

The most important thing here is `{{name}}`. We took our variable `name` and put it to the text string.
And the user will see something like `Hello, Alexander!`.

Now, convert the file to a shortcut:

```bash
shortcuts t.toml t.shortcut
```

And open the `t.shortcut` file in the Shortcuts app.

## Full toml file

```toml
[[action]]
type = "ask"
question = "What is your name?"

[[action]]
type = "set_variable"
name = "name"

[[action]]
type = "show_result"
text = "Hello, {{name}}!"
```

Description of all supported actions you can find here: [/docs/actions.md](/docs/actions.md).

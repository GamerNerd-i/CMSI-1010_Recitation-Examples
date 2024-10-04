# Programming Strategy

Programming can be hard, and that's okay! The purpose of this brief file is to give you a strategy you can apply to any programming problem, from your first assignments in CMSI 1010 all the way through the more expansive problems in later classes.

Although written here from the perspective of doing your Problem Sets, it certainly applies to practical programming as well, especially debugging. Every bug is a programming problem you haven't solved yet!

## Identify the problem

What's the question asking? Even if the task is given, this might be harder to answer than you think. Simple tasks might have a lot of considerations when you're just starting out and are unfamiliar with what languages can do. Things like syntax, logic, and language features eventually become second nature, but until then just take it slow. As assignments get bigger, they inevitably have more moving parts, and the answer to the question of "what do I have to do here?" expands with them.

For example, let's say you want to build a calculator that you can run from the terminal. Well, that sounds easy enough! Python already handles numbers (`ints` and `floats`) and basic math operations (addition, subtraction, multiplication, division, exponentiation) on its own. You just need to use`input()` to take in the calculations, right? *Not quite!* Remember that `input()` takes in <u>strings</u>, which you can't do math on. You also need to consider what happens if they type letters instead of just numbers and symbols. Already, our problem is much more complex than we thought.

## Come up with an idea/strategy

I cannot stress enough the importance of *problem-solving* when programming. When the problem is brand-new, it's not a good idea to just jump straight into coding. If you do, you're likely to hit a wall somewhere because of an issue or test case you didn't previously identify, and may have to rewrite a lot of previous code to fix it.

### Break up the problem into subproblems

You know what the problem is. Most likely, it's not something that can be solved with just one or two lines of code. Take time to look at the problem from a procedural standpoint. What problems do you need to solve at each step? What problems do *those* problems have?

Don't even try to put it into code or pseudocode yet. If you take nothing else from this guide, remember this: ***When in doubt, draw it out!*** It's corny, yes, but that just means it'll stick better in your head.

### Write down all the steps

*Don't be afraid to write things down!* Programming deals with a lot of abstract concepts that float around until you put them down somewhere. Your code should *not* be the first place they come down. Have a list of steps somewhere for you to follow one-by-one. They don't even need to be text! Little doodles are fantastic for breaking down a problem into its basic parts, especially if it's a task you already do by second nature; if it's that familiar, there's a good chance you don't even think about a lot of the little details!

*This* is the point for you to start writing pseudocode and thinking about how you'd tell the computer to do things. But *don't write any actual code yet!* Get your whole process down first so you can follow it all the way through.

## Write the code

Notice how much thinking we've done before even trying to touch actual code? It's just like writing an academic paper: you need to (or should) do your research, formulate an argument, and create an outline first. *Then* you can pop open your word processor and start banging it out. Programming is much the same!

Your list should help you know where to start. Some things you can do in chronological order, but others will need some other "infrastructure" first. Just take things one at a time in whatever order makes sense.

## Test it

Testing is the most important part of programming. You *ALWAYS* need to make sure that your solution works -- for as many situations as you can possibly think of. Particularly weird or unconventional situations are called *edge cases*, and these are the ones you really want to check for.

Here are some common edge cases to look for as you move through this course:

* What if you get a negative number instead of a postive one?
* What if you get letters instead of a number? Or a number instead of letters?
* What if you get nothing when you expect something? Or if you get something when you expect nothing?

**Remember: Testing isn't one and done.** It's a process, and it's highly unlikely that you'll ever get all your test cases -- and all your edge cases -- on the first try! Which leads us to the last step...

## Evaluate

Your tests always result in one of two things...

### Success

To be blunt, you're usually not going to get this on the first try. If you do... Well, the joke goes that there's DEFINITELY something wrong if you get your code working correctly the first time.

Always make sure to test well. It's worth going back to your tests and checking for edge cases like I mentioned above, or even adding more tests.

But hey, if you're **really** sure, then well done!

### Fail, and repeat

Quite frankly, this is what you should expect the first time. I don't mean that in a depressing or discouraging way; ti's just the nature of problem solving and experimentation.

There are two kinds of errors you might get:

* **Syntax errors** mean that your code was typed wrong. You misspelled a name, forgot to indent, left a parenthesis open, etc.
* **Logical errors** mean that something about your logic - your solution - was wrong. Your code ran, but you got the wrong answer.

Some things to consider in your repeat run:

#### What went wrong?

Check the error logs. Your editor will usually throw a tantrum if you have a syntax error, both on-run and while you're coding. Logical errors aren't thrown with a big block of red text like syntax errors are, unless you're using an `assert()` statement to test.

#### Where did it go wrong?

For syntax errors, this is as simple as reading the error and finding the line number.

For logical errors, think about your steps and check the code at each point. `print()` is your best friend for checking what's going on at every step of execution.

#### How do I fix it?

Syntax errors have the solution clear-cut in their error, so just go in and fixing the code accordingly.

For logical errors, you may need to re-evaluate your code, your steps, or both. Every logical error is different, so there's no one-size-fits-all recommendation I can make. If you get stuck, it won't hurt to have someone else look at it, whether that's a friend, tutor, or teacher.

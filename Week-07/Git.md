# Git and GitHub

If you're reading this, you're probably reading it on GitHub. Hopefully, by now you recognize that GitHub is a "cloud storage" database for code, like a specialized version of Google Drive or Microsoft OneDrive.

**GitHub** and **git** are not the same thing; they are two individual programs that work very closely together. Google Docs/Slides/Sheets and Google Drive are not the same thing, but they are naturally integrated with each other.

GitHub is what's called a *version control* system.

> **[Version control](https://en.wikipedia.org/wiki/Version_control)** is the practice of controlling, organizing, and tracking the versions of files.

Google Drive applications have much smaller version control systems built in which allow you to revert a document to a previous save (Go look: it's the clock-arrow icon in the top right corner). For example, if you revise the paragraph of an essay in Google Docs but decide your previous wording was better, you can use the version control to revert the document to that previous state. GitHub serves the same purpose, but has a vastly expanded toolset to better suit writing code.

## Git Locations

Before we get into git's commands, I'd like to tell you about how it's structured. This hopefully will provide some context to what you're doing when you "add, commit, and push" your code.

First, your computer is its own space that has three segments: the *workspace*, the *index*, and the *local repository*.You'll mainly be concerned about the *workspace* and the *local repository*; the index isn't something we need to talk about.

* The *workspace* is wherever you're working right now. In Google Colab, your specific notebook would be your workspace. Moving forward, your Problem Set workspace will be your text editor (presumably Visual Studio Code).
* The *index* is a middle ground between the workspace and local repository. It's a "staging ground" for code you're pretty sure is okay, but want to check one last time before pushing.
* The *local repository* (local) is the most recent "confirmed" version of the code you're working on. Code here is presumably ready to be put on GitHub.

Second, *GitHub*, as you know, is the cloud. We often refer to it as **remote**. Remember that *what you see in local is not automatically updated on remote*. If your code is not on GitHub, your professors and the TA's cannot see it. **Always rememeber to make sure that your most recent commits are on GitHub by going directly to the [repository on the GitHub website](https://github.com/) to double check.**

### Cargo Plane Analogy

Think of Git as a system that (mostly) mirrors the journey of a package you send through the mail. I'll reference the image below as we go through the examples, so keep it in mind if it helps you understand what's happening.

![Cargo plane analogy for Git commands](Images/Assets/airport.png)

## Git Commands and Moving Code

### `status` - Check Current State

Before we start walking through each Git command, let's talk about a command that you can use at any point to understand where you are in the process.

> `git status` shows you the current state of your code in version control. This includes what "stage" of the process that you have code in, the number of lines changed, and any files that were added, changed, or removed since the previous version.

This is your flight schedule. Anything you need to know about your package-in-transit can be found here. You'll probably use it frequently in the beginning, and use it less as you get more comfortable with the system. Still, there's no harm in checking often!

### Outgoing Changes

#### `add` - Prepare Suggested Changes

#### `commit` - Solidify Local Changes

#### `push` - Send Local Changes to Remote

### Incoming Changes

#### `clone` - Retrieve Remote Repository

#### `pull` - Update Local with Remote Changes

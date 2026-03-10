# Notes

My notes and ramblings following along the ugit tutorial.

## Change 1 - ugit: DIY Git in Python

**Mon 09 March 2026 2:22am**

- A Version Control System (VCS) tracks, records, and manages changes to files. The most famous one is of course [Git](https://git-scm.com/).
  - And in the spirit of the [origin of the name](https://about.gitlab.com/blog/celebrating-17-years-of-git/#the-origin-of-the-name-git), I've decided that this toy implementation will be called [twit](README.md).
- So far the tutorial seems simple enough, nothing I haven't come across while using Python.
- I also learned a little bit more about the `.gitignore`. My virtual enviroment for this project is called `twitenv`, and I was going to add it to the `.gitginore` like this:
  - `*twitenv/`
  - Appearantly this is not exactly correct, because it ignores everything that ends in -`twitenv/`. Already learning new things.
- Why am I up so late? Becuase I have a procrastination problem (also I hate daylight savings!!).  
- `pip install -e .` will install the "editable" version of the software in our current directory. The command for getting "Hello, World!" given in the tutorial is now outdated.
- I added a `project.toml` to make things more modern. 
- I now have a few todos:
  - [ ] TODO: Explain why and how `project.toml` works
  - [ ] Add a GitHub workflow for versioning and releases

## Change 2 - cli: Add arguement parser

**Mon 09 March 2026 9:19pm**

- I'm quite familiar with argparse since I've used it for making clis at my varying internships. Nothing too crazy!

## Change 3 - init: Create new .ugit directory

**Mon 09 March 2026 11:09pm**

- There's something really exciting about building a variation of a tool you use daily. It demistifies a lot of the magic/power these tools have, and somewhat transfers that power to the user. Seeing how the sausage is made as they say.
- This change introduces the `data.py` file which makes the twit repository for a given project. Very coool.

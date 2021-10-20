## Contributing Guidelines

All changes happen through pull requests. Pull requests are the best way to propose
changes. We actively welcome your pull requests and invite you to submit pull requests
directly [here](https://github.com/aryaniyaps/flamiche/pulls), and after review,
these can be merged into the project.


## First time setup
- Download and install the [latest version of git](https://git-scm.com/downloads).
- Configure git with your
  [username](https://docs.github.com/en/github/using-git/setting-your-username-in-git)
  and [email](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address).

    ```text
    $ git config --global user.name 'your name'
    $ git config --global user.email 'your email'
    ```

- Make sure you have a [GitHub account](https://github.com/join).
- Fork Flamiche to your GitHub account by clicking the
  [Fork](https://github.com/aryaniyaps/flamiche/fork) button.
- [Clone](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#step-2-create-a-local-clone-of-your-fork)
  the main repository locally.

    ```text
    $ git clone https://github.com/aryaniyaps/flamiche
    $ cd flamiche
    ```

- Add your fork as a remote to push your work to. Replace
    ``{username}`` with your username. This names the remote "fork", the
    default Flamiche remote is "origin".

    ```text
    $ git remote add fork https://github.com/{username}/flamiche
    ```

  - Create a virtualenv.
    - `Linux/ MacOS`
      ```text
      $ python3 -m venv env
      $ . env/bin/activate
      ```

    - `Windows OS`
      ```text
      > py -3 -m venv env
      > env\Scripts\activate
      ```

- Upgrade pip and setuptools.

    ```text
    $ python -m pip install --upgrade pip setuptools
    ```

- Install the development dependencies, then install Flamiche in editable mode.

    ```text
    $ pip install -r requirements/dev.txt && pip install -e .
    ```

- Install the pre-commit hooks.

    ```text
    $ pre-commit install
    ```

## Start coding

- Create a branch to identify the issue you would like to work on.

    ```text
    $ git fetch origin
    $ git checkout -b your-branch-name origin/main
    ```

- Using your favorite editor, make your changes,
    [committing as you go](https://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html#commit-your-changes).
- Include tests that cover any code changes you make. Make sure the
    test fails without your patch. Run the tests as described below.
- Push your commits to your fork on GitHub and
    [create a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request). Link to the issue being addressed with
    ``fixes #123`` in the pull request.

    ```text
    $ git push --set-upstream fork your-branch-name
    ```

    If this is your first contribution to this repository, don't
    forget to add your name to the [contributors list](CONTRIBUTORS.md).

## Running the tests

Run the basic test suite with pytest
(assuming that test dependencies have been installed).

```text
$ pytest
```

This runs the tests for the current environment, which is usually
sufficient. CI will run the full suite when you submit your pull request.
You can run the full test suite with tox if you don't want to wait.

```text
$ tox
```

## License

By contributing to Flamiche, you agree that your contributions will be licensed
under the [license file](LICENSE).

# Contributing to `titans`

## Installation for Development

To install `titans` for development, include the `dev` extras and the `-e` option,
which will install the project in editable mode.

```bash
pip install -e .[dev]
```

It is recommended that you install pre-commit into your git hooks, to automatically
check and fix any formatting issue before creating a git commit.

To enable pre-commit simply run:

```bash
pre-commit install
```

See the `.pre-commit-config.yaml` configuration file for more information on how it works.  

## Contributing Code

The `titans` repository utilizes the [GitFlow](https://datasift.github.io/gitflow/IntroducingGitFlow.html) workflow for code contributions.
Another more detailed [reference](https://nvie.com/posts/a-successful-git-branching-model/).  

The basic idea is as follows. `master` and `develop` are protected branches that can not be modified directly. Instead, to make a change,
branches are made off of one of `develop` or `master`, then a merge request is created into the appropriate branch.

NOTE: This is a solo recreation of the project, so GitFlow is not adhered to with concern to merge requests.  

### Contributing a Feature/Change into `develop`

The typical workflow involves makes changes (features, bug fixes, code enhancements, 
documentation) into the `develop` branch. To do this:

1. create a branch off of `develop` (name it anything except `master`, `develop`)
2. commit changes to that branch
3. create a merge request back into `develop`

A typical workflow:

```bash
git checkout develop

# ensure you are up to date
git pull

git checkout -b my-awesome-feature

# ...make changes to code
git commit -m "creating interface"
git commit -m "implementing some functions"

# whenever new changes appear in develop, get up to date
git checkout develop
git pull
git checkout my-awesome-feature
git merge develop

# ...make more changes to code
git commit -m "adding tests"
git commit -m "fixing a bug"

git push origin my-awesome-feature

# go to `https://github.com/lucasfzhou/titans-ml` and create a merge request
```

### Creating a Merge Request

This should be pretty straightforward. Be sure to make a thorough description of the
changes made and how they have been tested, if relevant. Some things to remember:
- be sure to reference any issues resolved by the new changes
- use the `Draft: ` prefix to create a work-in-progress merge request. This makes it easy
for others to track and visualize your work before it is complete  

### Reviewing Merge Requests

The following things may be repeated until at least one contributer who is not the
original author approves of the merge request: 

- suggest changes by making comments
- if something seems small and would be easier to just do yourself, feel free to make
the change directly on the branch
- if you would like to make a change yourself but it is a major change or feature in
its own right, instead create your own branch off of the feature branch and make a merge request back into that branch   

## Testing

`titans` uses the python standard library [unittest](https://docs.python.org/3/library/unittest.html) framework.  

To run all unit tests, execute:

```bash
bash run_tests.sh
```

To run a specific test, execute:

```bash
python tests/<file>.py
```

To run a specific test case, execute:

```bash
python tests/<file>.py <TestClass>>.<test_method>
```

For example:

```bash
python tests/test_tfefficientnet.py TestEfficientNet.test_label_map
```
  
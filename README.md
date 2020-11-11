# mrunner

mrunner is a tool intended to run experiment code on different
computation systems, without manual deployment and with significantly
less configuration. Main features are:

- Prepare remote environment,
- Deploy code,
- Run experiments,
  - Use of scheduler like Slurm or Kubernetes on the remote,
  - It is also possible to run experiment locally.
- Monitor experiments using [neptune](neptune.ml).

Currently [slurm](https://slurm.schedmd.com) and _(possibly)_
[kubernetes](http://kubernetes.io) clusters are supported.

## Install

Run `pip install .` in the repo root dir after cloning it.

## How to use?

More details may be found in the [examples](examples).

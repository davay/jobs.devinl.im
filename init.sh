#!/bin/bash

uv python install 3.11

(
  cd web || exit
  pnpm install
)

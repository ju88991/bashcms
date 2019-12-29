#!/bin/bash -euvx
source "$(dirname $0)/conf"
exec 2> "$logdir/$(basename $0).$(date +%Y%m%d_%H%M%S).$$"

dir="$(tr -dc 'a-zA-Z0-9_=' <<< ${QUERY_STRING} | sed 's;=;s/;')"

md="$contentsdir/posts/template/main.md"
[ -f "$md" ]

pandoc --template="$viewdir/template.html" -f markdown_github+yaml_metadata_block "$md"


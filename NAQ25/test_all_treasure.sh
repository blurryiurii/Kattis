for ROW in {1..4}; do
  for COL in {1..4}; do
    echo \# $ROW $COL
    python3 testing_tool.py -r $ROW -c $COL python3 k.py || break
  done
done
for FILE in *_april_temps_1950-2018.csv
do
  ABB=$(basename ${FILE} _april_temps_1950-2018.csv)
  python calculate_mean.py ${FILE} ${ABB} ${1}
done

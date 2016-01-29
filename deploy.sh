source ~/venv/bin/activate
echo "activating virtualenv"
git pull
python manage.py collectstatic
cd ..
rm tmp/restart.txt
touch tmp/restart.txt
echo "deploy complete"


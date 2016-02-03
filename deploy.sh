source ~/venv/bin/activate
echo "activating virtualenv"
git pull
python manage.py collectstatic --noinput
cp -r ~/brobin.me/brobin/brobin/static/ ~/brobin.me/public
python manage.py migrate
cd ..
rm tmp/restart.txt
touch tmp/restart.txt
echo "deploy complete"


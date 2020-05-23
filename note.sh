# Add this function to your .bash_profile

note(){
   dir="$(pwd)"
   cd /YOUR/PATH/OF/WHERE/NOTEPY/IS/SAVED
   python notepy.py $dir $1
   cd
   cd $dir
}
# tabular-workshop

###  Pre-Requisites:

---

 * I built this on a new install of Ubuntu Server
 * Version: 20.04.5 LTS 
 * Instance Specs: (min 4 core w/ 16 GB ram & 30 GB of disk) -- add more RAM if you have it to spare.
 * If you are going to test this in `AWS`, it ran smoothly for me using AMI: `ami-03a311cadf2d2a6f8` in region: `us-east-2` with a instance type of: `t3.xlarge`

---
### Create OS User `Datagen` 

*  This user account will be the owner of all the objects that get installed
*  Security is not in place for any of this workshop.

```
##########################################################################################
#  create an osuser datagen and add to sudo file
##########################################################################################
sudo useradd -m -s /usr/bin/bash datagen

echo supersecret1 > passwd.txt
echo supersecret1 >> passwd.txt

sudo passwd datagen < passwd.txt

rm -f passwd.txt
sudo usermod -aG sudo datagen
##########################################################################################
#  let's complete this install as this user:
##########################################################################################
# password: supersecret1
su - datagen 
```
---

###  Install Git tools and pull this repo.
*  ssh into your new Ubuntu 20.04 instance and run the below command:
 
---
```
sudo apt-get install git -y

cd ~
git clone https://github.com/tlepple/tabular-workshop.git
```

---

### Start the build:

```
#  run it:
. ~/tabular-workshop/setup.sh
```
  *  This should complete within 10 minutes.
---

---

If you have made it this far, I want to thank you for spending your time reviewing the materials. Please give me a 'Star' at the top of this page if you found it useful.

---
---

####  Extra Credit

* Interested in exploring the underlying PostgreSQL Databases for `datagen`?
[Explore Postgresql](./explore_postgresql.md)

---
---

  ![](./images/drunk-cheers.gif)

[Tim Lepple](www.linkedin.com/in/tim-lepple-9141452)

---
---

#simple method to change user email from old domain to new domain
def replaceDomain(email, oldDomain, newDomain):
  if '@' + oldDomain in email: 
    index=email.index('@' + oldDomain)
    newEmail=email[:index]+'@'+newDomain
    return newEmail
  return email
  
#calling task
print(replaceDomain('shifatjahan.hcc@gmail.com','gmail.com','iit.du.ac.bd'))

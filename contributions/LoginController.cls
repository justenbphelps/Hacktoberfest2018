public with sharing class LoginController {
    public contact reg { set; get;}
    public List<contact> user{get; set;} 
    public String passcode{get; set;}
    public Boolean Match{get; set;}
    public Boolean NoMatch{get; set;}


    public LoginController() {
        reg = new contact();
    }
    Public PageReference signin(){
        user = new List<contact>();
        Match = false;
        NoMatch = false;
        user = [select Username__c,Password__c from contact where Username__c =: reg.Username__c AND Password__c =:reg.Password__c limit 1];
        if(user.size()>0)
        {
            Match = true;
        }
        else{
            NoMatch = true;
        }
        PageReference pageref = new PageReference('Apex Page');
        pageref.setRedirect(true);
        return pageref;
    }
    public Pagereference doCancel(){
        PageReference pageref = new PageReference(' Apex Page ');
        pageref.setRedirect(true);
        return pageref;
        
    }
}
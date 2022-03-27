# Apk-Modding-challenge
30 days | 30 small apks around 10-20Mb not >30 

ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ

### Goal - <img src="https://img.shields.io/static/v1?label=&message=Smali&color=important&style=plastic&logoColor=violet" width="30" height="15"> knowledge is must
   - [x] *Remove Ads*
   - [x] *Bypass In-app purchase*


ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ

### Requirements

   - [x] Apktool
    
### Inspired by Bin32, apkunpacker, euzada & many pro guys 🧠...
ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ



*Day 1*
   
   **Resistor Color Code Calculator**
   
   ![Screenshot_20220318-101945_Google Play Store](https://user-images.githubusercontent.com/62318734/158939543-ea2a7b37-3108-4456-9e93-79a7f63895e2.png)
ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ

<h3><b>Solution</b></h3>

 -  *Decompile the apk*
 -  *Use grep for searching stuffs*
 -  *Any text editor in my case i used **vim** coz its cool.*
 -  *using sed & awk is optional*
 -  *Modify the code*
 -  *Recompile*

<p>For this apk got some interesting stuffs from resource.arsc<br></p>

   ![20220319_105716](https://user-images.githubusercontent.com/62318734/159108433-f258a81e-1489-4325-87dd-3f041b17929c.png)
   
   - <ins>***res/values/strings.xml:    <string name="usuario_premium">Premium User</string>***</ins> its corresponding hex Id <ins>**0x7f0e009b**</ins>
   
   - `grep -ir 0x7f0e009b tmp --color`

   ![20220319_152200](https://user-images.githubusercontent.com/62318734/159116412-c76829bf-e8e9-457a-a9a0-430b867403e1.png)
   
 
<h4><b>two methods</b></h4>

   
   ![20220319_153423](https://user-images.githubusercontent.com/62318734/159116731-83b06779-c110-451d-9282-c554067aaf5a.png)
   
   - **Method 1**
      
      
      - *change boolean to **TRUE** by replacing move-result v3 to const/4 v3, 0x1*

   - **Method 2**

       
      - *goto com/jedemm/resistorcalculator/App$a*

      ![20220319_155924](https://user-images.githubusercontent.com/62318734/159117464-1b078ec4-3c93-4bb5-8692-aaf5883d4391.png)


      - *replace **sget-boolean** to **sput-boolean** and add const/4 v0, 0x1 below **.locals 1****

     - *Recompile it using apktool*

![Screenshot_20220319-160846_RCC Calculator](https://user-images.githubusercontent.com/62318734/159117699-29e1d203-b0cb-4e63-9e13-da7e958a6faa.png)
![Screenshot_20220319-160852_RCC Calculator](https://user-images.githubusercontent.com/62318734/159117704-9d21a35d-43aa-49cb-9c8d-199ed3e59cf0.png)



 ## 2nd
 
   ![Screenshot_20220324-170306_Google Play Store](https://user-images.githubusercontent.com/62318734/159907680-c25ceada-a5ed-4708-9cda-89bb9977c186.png)
   
   <h3><b>Solution</b></h3>
       
       
   [![000](https://user-images.githubusercontent.com/62318734/159939739-4284d286-f927-4b4a-9be3-b43575fe8b9d.png)](https://user-images.githubusercontent.com/62318734/159942517-bac17e27-40b1-4e03-8bab-c2c1e0c69283.mp4)
   
   ### Unlocking Gold theme
   
   ![20220324_224520](https://user-images.githubusercontent.com/62318734/159974165-bcfe54dc-b01b-4975-8e3c-1ea95cbbb0b9.png)

   
   - <ins>***com/aefyr/sai/billing/DonationStatus.smali***</ins>

   ![20220324_225551](https://user-images.githubusercontent.com/62318734/159975085-d8afcdae-4fb0-4b73-b1ca-e8a40f0a829f.png)

            
     
     
     
     
     
   - ***change if-ne to if-eq or if-ne p0 to if-eqz***

        ![20220324_232334](https://user-images.githubusercontent.com/62318734/159980184-ecad9cf5-e119-413c-8406-b7e6543fdb22.png)

  
  
### Hide ***Support Sai***

           
           
   ![20220324_230812](https://user-images.githubusercontent.com/62318734/159977158-bbb2e0fa-a757-43ad-a045-2874e41f0ce1.png)
   
   - ***com/aefyr/sai/ui/fragments/PreferencesFragment.smali***

![20220324_231658](https://user-images.githubusercontent.com/62318734/159978548-26c634f0-9cc4-46cf-8d1b-ee98a86d5748.png)


   - **change ***const/4 p2, 0x1 to const/4 p2, 0x0*****

      ![20220324_232356](https://user-images.githubusercontent.com/62318734/159979958-1c1c7b3a-bbfe-420a-a374-a5bab0fdc181.png)


### 3rd 

 ![Screenshot_20220324-234704_Google Play Store](https://user-images.githubusercontent.com/62318734/159987415-19a7b044-8f62-4d27-b9ec-4948252c28e6.png)


nothing in resource.arsc instead found ***donated3*** in smali*

![20220325_000444](https://user-images.githubusercontent.com/62318734/159987753-fc23fec5-95a1-40a0-8540-be08d28e0a16.png)

  -  goto <ins>***smali_classes2/com/silentlexx/ffmpeggui/config/Config.smali***</ins></br>
  
        ![20220325_001630](https://user-images.githubusercontent.com/62318734/159989232-3bdb4d80-0106-45d5-946e-6e0ce33abcec.png)

        - search for string ***donated3*** using vim regex
        - either change boolean false to true in ***getBool*** method or in ***getDonated*** method by changing **move-result** to **const/4** and set it to true*
        - recompile it
       

<h3><b>For signing use <ins>Uber-apk-signer</ins> but <ins>Google play protect</ins> warns.</b></br>
              
              
              
    instead you may use my keystore to sign apk to stop Google play protect warnings 
    
   ![20220325_005820](https://user-images.githubusercontent.com/62318734/159995288-1ae4ead1-c97b-4133-a268-b33a6285174b.png)

   ![20220325_005803](https://user-images.githubusercontent.com/62318734/159995403-1c4fca87-3485-4528-97a7-f89136dd35d6.png)


   ![Screenshot_20220325-010208_FFmpeg Media Encoder](https://user-images.githubusercontent.com/62318734/159995820-9ee06bb3-a3c6-41ef-92c8-b3fd40d9954a.png)


  
### 4th

   ![Screenshot_20220326-225540_Google Play Store](https://user-images.githubusercontent.com/62318734/160250653-10478016-6570-4e98-a847-00bbf3078e94.png)


   #### solution
   
     
   ![20220326_233829](https://user-images.githubusercontent.com/62318734/160251946-c83f0290-21da-418c-b72d-28c29a23dcc2.png)
   

   - ***<ins>smali/com/smokyink/smokyinklibrary/pro/licence/DefaultFeatureManager.smali</ins>***
   
   ![20220326_234751](https://user-images.githubusercontent.com/62318734/160252246-aac22194-48c0-45e9-91d4-0c0a7cbfe375.png)</br>
 
 
   - change *<b>nez</b>* to *<b>eqz</b>*. **Samething can be achieved by removing condition**
   - recompile

# Before
   ![20220327_001449](https://user-images.githubusercontent.com/62318734/160252995-9a44168e-c6aa-4bf7-90d7-9315b4c67b6e.png)
# After
   ![Screenshot_20220327-001547_Timeshift](https://user-images.githubusercontent.com/62318734/160253031-2bd89cc3-ac1e-4665-91e8-16ebeb2cae2c.png)
![Screenshot_20220327-001554_Timeshift](https://user-images.githubusercontent.com/62318734/160253039-e4f71025-2e5f-403e-b5b1-dfe49cde57e4.png)


# 5

![Screenshot_20220327-173523_Google Play Store](https://user-images.githubusercontent.com/62318734/160280662-f75678b2-c1d6-4c19-9e0b-94193c99f188.png)

![Screenshot_20220327-201000_WhatsApp](https://user-images.githubusercontent.com/62318734/160286773-dc671165-fb7f-4042-a2ac-8aa9eb41f894.png)

  ### solution
  
   - Decompile the apk 
   - search for this toast msg
   - find its id
   - search and change it

  <video  style="display:block; width:100%; height:auto;" autoplay controls loop="loop">
           <source src="/src/C5#1.mp4" type="video/mp4" />
           

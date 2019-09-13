# Sencha-ExtJS-basic-app
Sencha ExtJS basic app

For this to work you need to download and setup Sencha ExtJS 6.2.0, and Sencha CMD
### source: https://docs.sencha.com/cmd/guides/extjs/cmd_app.html
```
https://www.sencha.com/products/extjs/cmd-download/

https://docs.sencha.com/cmd/guides/intro_to_cmd.html
install ruby also

for android studio download and install android sdk, then setup the path

https://www.npmjs.com/get-npm

https://cordova.apache.org/#getstarted

add path environment variable to sencha cmd installation folder (where sencha.exe is)
```
```
java sdk 8 installed too - add JAVA_HOME C:\Program Files\Java\jdk1.8.0_191
```
```
install gradle or android  studio

For Windows:

-Download last version of Gradle (https://gradle.org/releases)

-Create a folder and unzip files (I use C:\Program Files (x86)\gradle)

-Copy the path with the bin directory included (C:\Program Files (x86)\gradle\bin)

-Set the path C:\Program Files (x86)\gradle\bin (in my exemple) to "Path Environment Variables"

Variable name "Path" and variable value "C:\Program Files (x86)\gradle\bin" for both: User Variable table and System Variables table

You may need to reopen the "Prompt commad line"

To test, type gradle in prompt.
```

## Generate app
```
This is run from project folder you want to setup Sencha Project at
```
```
sencha -sdk C:\path_to_Sencha_extjs\Sencha\ext-6.2.0 generate app -ext -modern MyApp ./

sencha -sdk C:\projects\Sencha\ext-6.2.0 generate app -ext -modern app_name ./
```

## Cordova and Sencha
After you setup Sencha project, you need to install cordova and setup cordova in same project by running the following command.
```
sencha cordova init com.mycompany.MyApp MyApp
```
```
sencha cordova init rs.infodata.MyApp MyApp
```
You also need to ensure that all dependecies are met to setup cordova (NodeJS, etc.)
### more information: https://cordova.apache.org/docs/en/latest/guide/cli/

Afterwards you need to ensure that Sencha app.json has this placed so when it builds it will use cordova for native packaging
```
Add to app.json cordova
"builds": {
    "native": {
        "packager": "cordova",
        "cordova" : {
            "config": {
                "platforms": "android"
                "id": "com.mydomain.MyApp"
            }
        }
    }
}
```

In cordova folder run this command to add platform for which we setup project. If you want specific android version supported add @ afterwards the version for android. Best is to avoid it.
Note for this to work you need to have proper SDK installed and/or Android Studio with SDK package. Google it.
```
cordova platform add android
```
cordova platform add android@4


In app.json place this code to include "css" route for project. I placed it in resources as you can see
```
,{"path":"/resources/css/main.css"}
```
Make sure there is  ,  if needed, otherwise the application will break and not run at all.


run in command promt
## sencha app watch


### Build apk
```
sencha app build native
```
You can change name of the build in app.json and which packager to use.


### Css i sass
```
sencha ant sass still works with cmd 6.5. Add development as sencha ant development sass to generate a readable .css
```

### Cordova supported sdk

### add in cordova/config.xml
```
    <platform name="android">
        <allow-intent href="market:*" />
        <preference name="android-targetSdkVersion" value="22" />
    </platform>
```


# Cordova plugins

```
cordova plugin add cordova-plugin-geolocation
```

## Notes za geolocation
```
Must have timeout or it will not show error, also will not work
```
### source: https://www.npmjs.com/package/cordova-plugin-geolocation
```
navigator.geolocation.getCurrentPosition(onSuccess, onError, { maximumAge: 1000, timeout: 25000, enableHighAccuracy: true });
```
```
OnSuccess is function that is run onSuccess, and onError is run when error is present, the last part is options passed as json. Note that you need to make those function.
```
### How to use:
```
var onSuccess = function(position) {
    new Ext.MessageBox().show({
        title: "onSuccess",
        message: 'Latitude: ' + position.coords.latitude + '\n' +
            'Longitude: ' + position.coords.longitude + '\n' +
            'Altitude: ' + position.coords.altitude + '\n' +
            'Accuracy: ' + position.coords.accuracy + '\n' +
            'Altitude Accuracy: ' + position.coords.altitudeAccuracy + '\n' +
            'Heading: ' + position.coords.heading + '\n' +
            'Speed: ' + position.coords.speed + '\n' +
            'Timestamp: ' + position.timestamp + '\n'
    })
};

// onError Callback receives a PositionError object
function onError(error) {
    new Ext.MessageBox().show({
        title: "onError",
        message: 'code: ' + error.code + '\n' +
            'message: ' + error.message + '\n'
    })
}

navigator.geolocation.getCurrentPosition(onSuccess, onError, { maximumAge: 1000, timeout: 25000, enableHighAccuracy: true });
```

## Launch navigator
### source: https://www.npmjs.com/package/uk.co.workingedge.phonegap.plugin.launchnavigator
```
Using native maps to navigate to cordinates
```

## Note for barcode-scanner
### source: https://www.npmjs.com/package/phonegap-plugin-wininsoft-barcodescanner
```
cordova plugin add phonegap-plugin-barcodescanner
```
### How to use:
```
cordova.plugins.barcodeScanner.scan(
    function(result) {
        new Ext.MessageBox().show({
            centered: true,
            title: "Result",
            message: "We got a barcode\n" +
                "Result: " + result.text + "\n" +
                "Format: " + result.format + "\n" +
                "Cancelled: " + result.cancelled
        })
    },
    function(error) {
        alert("Scanning failed: " + error);
    }, {
        preferFrontCamera: false, // iOS and Android
        showFlipCameraButton: true, // iOS and Android
        showTorchButton: true, // iOS and Android
        torchOn: false, // Android, launch with the torch switched on (if available)
        saveHistory: false, // Android, save scan history (default false)
        prompt: "Place a barcode inside the scan area", // Android
        resultDisplayDuration: 500, // Android, display scanned text for X ms. 0 suppresses it entirely, default 1500
        // formats: "QR_CODE,PDF_417", // default: all but PDF_417 and RSS_EXPANDED
        orientation: "portrait", // Android only (portrait|landscape), default unset so it rotates with the device
        disableAnimations: true, // iOS
        disableSuccessBeep: false // iOS and Android
    }
);
```

## Note for camera
### source: https://cordova.apache.org/docs/en/latest/reference/cordova-plugin-camera/#camera-getPicture-examples
### documentation: https://cordova.apache.org/docs/en/latest/reference/cordova-plugin-camera/
```
cordova plugin add cordova-plugin-camera
```

## Note for background upload
### source : https://www.npmjs.com/package/cordova-plugin-background-upload
```
cordova plugin add cordova-plugin-background-upload
```

### How to use:
```
let options = {
    quality: 100,
    destinationType: navigator.camera.DestinationType.FILE_URI,
    // destinationType: navigator.camera.DestinationType.DATA_URL,
    // destinationType: navigator.camera.DestinationType.NATIVE_URI,
    allowEdit: false,
    saveToPhotoAlbum: true,
    cameraDirection: 1,
    sourceType: navigator.camera.PictureSourceType.CAMERA,
};

// function to be run on success - it saves uri for image and afterwards sends it to server (tries at least)
function onSuccess(imageURI) {
    var store = Ext.getStore('Slike');
    if (!store) {
        store = Ext.create('Ext.data.Store', {
            alias: 'store.Slike',
            //mora da ima store id
            storeId: 'Slike',
            requires: [
                'Ext.data.proxy.LocalStorage',
                // "app_name.model.ImageModel"
            ],
            // model: 'app_name.model.ImageModel',
            fields: ['imageURI', 'sent'],
            proxy: {
                type: 'localstorage',
                reader: {
                    type: 'json',
                    rootProperty: 'result',
                }
            }
        });
    }
    //this records image uri and saves in store for sync to be run later with server
    store.add({
        imageURI: imageURI,
        sent: false
    })
    store.sync()
    var win = function(result) {
        console.log(JSON.stringify(result));
        Ext.Msg.alert(
            "success",
            result
        )
    }
    var fail = function(error) {
        console.log(JSON.stringify(error));
        Ext.Msg.alert(
            "error",
            error
        )
    }
    try {
        // for this to work you need to have following plugins in cordova
        // cordova-plugin-background-upload
        // cordova-plugin-file
        // cordova-plugin-file-transfer
        var uploader = FileTransferManager.init();
        uploader.on('success', function(upload) {
            Ext.Msg.alert("success", "upload: " + upload.id + " has been completed successfully");
            Ext.Msg.alert("upload", "code: " + upload.statusCode + " response:" + upload.serverResponse);
        });
        uploader.on('progress', function(upload) {
            Ext.Msg.alert("Alert", "uploading: " + upload.id + " progress: " + upload.progress + "%");
        });
        uploader.on('error', function(uploadException) {
            if (uploadException.id) {
                Ext.Msg.alert("Alert", "upload: " + uploadException.id + " has failed");
                /*
                // source: https://stackoverflow.com/questions/3501749/php-move-uploaded-file-error
                // Since it is in php code backend it will return the following errors
                UPLOAD_ERR_INI_SIZE = Value: 1; The uploaded file exceeds the upload_max_filesize directive in php.ini.

                UPLOAD_ERR_FORM_SIZE = Value: 2; The uploaded file exceeds the MAX_FILE_SIZE directive that was specified in the HTML form.

                UPLOAD_ERR_PARTIAL = Value: 3; The uploaded file was only partially uploaded.

                UPLOAD_ERR_NO_FILE = Value: 4; No file was uploaded.

                UPLOAD_ERR_NO_TMP_DIR = Value: 6; Missing a temporary folder. Introduced in PHP 5.0.3.

                UPLOAD_ERR_CANT_WRITE = Value: 7; Failed to write file to disk. Introduced in PHP 5.1.0.

                UPLOAD_ERR_EXTENSION = Value: 8; A PHP extension stopped the file upload. PHP does not provide a way to ascertain which extension caused the file upload to stop; examining the list of loaded extensions with phpinfo() may help.
                */

            } else {
                Ext.Msg.alert("error", "uploader caught an error: " + uploadException.error);
            }
        });
        // see source for more information
        var payload = {
            "id": imageURI.substr(imageURI.lastIndexOf('/') + 1),
            "name": imageURI.substr(imageURI.lastIndexOf('/') + 1),
            //name of file
            "fileName": imageURI.substr(imageURI.lastIndexOf('/') + 1),
            "filePath": encodeURI(imageURI.slice(7)),
            "fileKey": "file",
            "serverUrl": "http://localhost/filip/upload_1.php",
            chunkedMode: false,
        };
        uploader.startUpload(payload);
    } catch (error) {
        Ext.Msg.alert(
            "error",
            error
        )
    }
}

function onFail(message) {
    Ext.Msg.alert('Failed because: ' + message);

}
console.log('navigator', navigator);
// here I run code to take picture.
navigator.camera.getPicture(onSuccess, onFail, options);
```

## Note additional file managers
### source https://www.npmjs.com/package/cordova-plugin-file-transfer

## cordova-plugin-background-mode
### source: https://github.com/katzer/cordova-plugin-background-mode
If running Cordova 9:
    https://github.com/katzer/cordova-plugin-background-mode/issues/441


# Sencha memo

## Store
```
Must contain store id
```
```
var store = Ext.getStore('AllStreets');
if (!store) {
    store = Ext.create('Ext.data.Store', {
        alias: 'store.AllStreets',
        //Must contain store id
        storeId: 'AllStreets',
        requires: [
            'Ext.data.proxy.LocalStorage',
            "app_name.model.AllStreetsModel"
        ],
        model: 'app_name.model.AllStreetsModel',
        // fields: ['code', 'address', 'zone', 'region', 'id'],
        proxy: {
            type: 'localstorage',
            reader: {
                type: 'json',
                rootProperty: 'result',
            }
        }
    });
}
```
## Store
```
if (store.findRecord("sifra", record.get("sifra"),0,false, true, true)) {
//store.findRecord( fieldName, value, [startIndex], [anyMatch], [caseSensitive], [exactMatch] )
```

## Event listener
```
event listener za back i menu button
try{
    document.addEventListener("menubutton", adriatic.app.getController( 'adriatic.controller.MainController' ).menuButton, true);
    document.addEventListener("backbutton", adriatic.app.getController( 'adriatic.controller.MainController' ).backButton, true);
}
catch (error) {
    console.log('error:', error);
}
```
## Store proxy load
```
Ext.define('kuhinja.store.Orders', {
    extend: 'Ext.data.Store',
    alias: 'store.orders',
    requires: [
        'Ext.data.proxy.LocalStorage',
        'kuhinja.util.UrlData'
    ],
    config: {
        storeId: 'Orders'
    },
    proxy: {
         //async javascript anx xml
         type: 'ajax',
         method: 'get',
         url: UrlData.getOrders(),
         // for cors
         cors: true,
         // has to be set to false for cors to work
         useDefaultXhrHeader : false,
         reader: {
             type: 'json',
             // rootProperty: 'result'
         }
     },
     autoLoad: true
});
```
### Dataview
```
// On reload store scroll to top
scrollToTopOnRefresh: false
```

```
{novac:number("0,0.00")}
{novac:date("d-m-Y")}
```

## Errors
```
ERR: File not found - ako se javi nesto nije importovano u projekat
```
```
Na touch dupli klik ako se okida, prebaci da na dugme nije listener vec handler function
```


### Forms
```
var form = Ext.create('Ext.form.Panel', {

    requires: [
        'Ext.form.FieldSet',
        'Ext.field.Number',
        'Ext.field.Spinner',
        'Ext.field.Password',
        'Ext.field.Email',
        'Ext.field.Url',
        'Ext.field.DatePicker',
        'Ext.field.Select',
        'Ext.field.Hidden',
        'Ext.field.Radio'
    ],
    shadow: true,
    cls: 'demo-solid-background',
    id: 'basicform',
    closable: true,
    centered: true,
     modal: true,
     fullscreen: true,
     // frame: true,
     title: 'Izmena',
     layout: 'vbox',
     bodyPadding: 10,
     scrollable: true,
     width: '90%',
     height: '90%',
     overflow: 'scroll',
     overflow: 'scrollable',
     autocomplete: false,
     autocomplete: 'off',

     fieldDefaults: {
         labelAlign: 'right',
         labelWidth: 115,
         msgTarget: 'side'
     },
    items: [
        {
            xtype: 'fieldset',
            id: 'fieldset1',
            title: 'Personal Info',
            instructions: 'Please enter the information above.',
            defaults: {
                labelWidth: '35%'
            },
            items: [
                {
                    xtype: 'textfield',
                    name: 'name',
                    label: 'Name',
                    placeHolder: 'Tom Roy',
                    autoCapitalize: true,
                    required: true,
                    clearIcon: true
                },
                {
                    xtype: 'passwordfield',
                    revealable: true,
                    name : 'password',
                    label: 'Password',
                    clearIcon: true
                },
                {
                    xtype: 'emailfield',
                    name: 'email',
                    label: 'Email',
                    placeHolder: 'me@sencha.com',
                    clearIcon: true
                },
                {
                    xtype: 'urlfield',
                    name: 'url',
                    label: 'Url',
                    placeHolder: 'http://sencha.com',
                    clearIcon: true
                },
                {
                    xtype: 'spinnerfield',
                    name: 'spinner',
                    label: 'Spinner',
                    minValue: 0,
                    maxValue: 10,
                    clearable: true,
                    stepValue: 1,
                    cycle: true
                },
                {
                    xtype: 'checkboxfield',
                    name: 'cool',
                    label: 'Cool',
                    platformConfig: {
                        '!desktop': {
                            bodyAlign: 'end'
                        }
                    }
                },
                {
                    xtype: 'datepickerfield',
                    destroyPickerOnHide: true,
                    name: 'date',
                    label: 'Start Date',
                    value: new Date(),
                    picker: {
                        yearFrom: 1990
                    }
                },
                {
                    xtype: 'selectfield',
                    name: 'rank',
                    label: 'Rank',
                    options: [
                        {
                            text: 'Master',
                            value: 'master'
                        },
                        {
                            text: 'Journeyman',
                            value: 'journeyman'
                        },
                        {
                            text: 'Apprentice',
                            value: 'apprentice'
                        }
                    ]
                },
                {
                    xtype: 'sliderfield',
                    name: 'slider',
                    label: 'Slider'
                },
                {
                    xtype: 'togglefield',
                    name: 'toggle',
                    label: 'Toggle'
                },
                {
                    xtype: 'textareafield',
                    name: 'bio',
                    label: 'Bio'
                }
            ]
        },
        {
            xtype: 'fieldset',
            id: 'fieldset2',
            title: 'Favorite color',
            platformConfig: {
                '!desktop': {
                    defaults: {
                        bodyAlign: 'end'
                    }
                }
            },
            defaults: {
                xtype: 'radiofield',
                labelWidth: '35%'
            },
            items: [
                {
                    name: 'color',
                    value: 'red',
                    label: 'Red'
                },
                {
                    name: 'color',
                    label: 'Blue',
                    value: 'blue'
                },
                {
                    name: 'color',
                    label: 'Green',
                    value: 'green'
                },
                {
                    name: 'color',
                    label: 'Purple',
                    value: 'purple'
                }
            ]
        },
        {
            xtype: 'container',
            defaults: {
                xtype: 'button',
                style: 'height: 60px;margin: 1em',
                flex: 1
            },
            layout: {
                type: 'hbox'
            },
            items: [
                {
                    text: 'Disable fields',
                    ui: 'action',
                    scope: this,
                    hasDisabled: false,
                    handler: function(btn){
                        var fieldset1 = Ext.getCmp('fieldset1'),
                            fieldset2 = Ext.getCmp('fieldset2');

                        if (btn.hasDisabled) {
                            fieldset1.enable();
                            fieldset2.enable();
                            btn.hasDisabled = false;
                            btn.setText('Disable fields');
                        } else {
                            fieldset1.disable();
                            fieldset2.disable();
                            btn.hasDisabled = true;
                            btn.setText('Enable fields');
                        }
                    }
                },
                {
                    text: 'Reset',
                    ui: 'action',
                    handler: function(){
                        Ext.getCmp('basicform').reset();
                    }
                }
            ]
        }
    ]
});
 Ext.Viewport.add(form)
```

## Component query - for tables
Gets every button with id like
```
var buttons = Ext.getCmp('tables').query('button[id^=id_]');
Ext.Array.each(buttons, function(button) {
    button.setCls("adderButton");
});
```

# Replace all ocurances of char in string - Javascript
```
str.replace(/,/g, "") - removes , with empty or deltes it
```

# Config.xml - for clear text error and orientation
```
add to top of config.xml
xmlns:android="http://schemas.android.com/apk/res/android"
```
```
    <preference name="Orientation" value="portrait" />
    <platform name="android">
        <uses-permission android:name="android.permission.INTERNET" />
        <edit-config file="AndroidManifest.xml" mode="merge" target="/manifest/application">
            <application android:usesCleartextTraffic="true" />
        </edit-config>
```
## Add network_security_config.xml to cordova/res/xml
```
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">192.168.0.89 </domain>
        <domain includeSubdomains="true">10.100.100.60 </domain>
        <domain includeSubdomains="true">localhost </domain>
        //allowed domains
    </domain-config>
</network-security-config>
```
### Cors
```
 xhr_art.setRequestHeader("Access-Control-Allow-Origin", "*");
            // xhr_art.setRequestHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept, Authorization");
```


### Cordova push notification
```
https://github.com/katzer/cordova-plugin-local-notifications
cordova plugin add cordova-plugin-local-notification
```
```

https://cordova.apache.org/docs/en/latest/reference/cordova-plugin-dialogs/index.html
cordova plugin add cordova-plugin-dialogs
```

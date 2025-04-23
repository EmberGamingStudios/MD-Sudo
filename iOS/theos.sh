#!/bin/bash

set -e

APP_NAME="Game"
BUNDLE_ID="com.yourname.game"

echo "Setting up Theos-compatible iOS app project..."

cat > XXAppDelegate.h <<EOF
#import <UIKit/UIKit.h>

@interface XXAppDelegate : UIResponder <UIApplicationDelegate>
@property (strong, nonatomic) UIWindow *window;
@end
EOF

cat > XXAppDelegate.m <<EOF
#import "XXAppDelegate.h"
#import "XXRootViewController.h"

@implementation XXAppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    self.window.rootViewController = [[XXRootViewController alloc] init];
    [self.window makeKeyAndVisible];
    return YES;
}

@end
EOF

cat > XXRootViewController.h <<EOF
#import <UIKit/UIKit.h>

@interface XXRootViewController : UIViewController
@end
EOF

cat > XXRootViewController.m <<EOF
#import "XXRootViewController.h"

@implementation XXRootViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.view.backgroundColor = [UIColor blackColor];

    UILabel *label = [[UILabel alloc] initWithFrame:self.view.bounds];
    label.text = @"Ren'Py Game Loaded!";
    label.textColor = [UIColor whiteColor];
    label.textAlignment = NSTextAlignmentCenter;
    [self.view addSubview:label];
}

@end
EOF

if [ -f main.c ]; then
    mv main.c main.m
    echo '#import <UIKit/UIKit.h>' | cat - main.m > temp && mv temp main.m
    echo '#import "XXAppDelegate.h"' | cat - main.m > temp && mv temp main.m
    sed -i '/main/ a return UIApplicationMain(argc, argv, nil, NSStringFromClass([XXAppDelegate class]));' main.m
fi

cat > Makefile <<EOF
TARGET := iphone:clang:latest:13.0
ARCHS = arm64

APPLICATION_NAME = ${APP_NAME}
${APP_NAME}_FILES = main.m XXAppDelegate.m XXRootViewController.m VideoPlayer.m Log.m IAPHelper.m
${APP_NAME}_FRAMEWORKS = UIKit Foundation AVFoundation
${APP_NAME}_RESOURCES = LaunchImage-*.png

include \$(THEOS)/makefiles/common.mk
include \$(THEOS_MAKE_PATH)/application.mk
EOF

mkdir -p DEBIAN
cat > control <<EOF
Package: ${BUNDLE_ID}
Name: ${APP_NAME}
Version: 0.01
Architecture: iphoneos-arm
Description: iOSGame
Maintainer: YourName
Author: YourName
Section: Games
EOF

echo "Project structure ready for Theos!"
echo "Run: make package"

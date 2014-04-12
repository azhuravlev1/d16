//
//  ZMAppDelegate.m
//  Magnets
//
//  Created by zaxdo on 12.04.14.
//  Copyright (c) 2014 zaxdo. All rights reserved.
//

#import "ZMAppDelegate.h"
#import "ZMMyScene.h"

@implementation ZMAppDelegate

@synthesize window = _window;

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
    /* Pick a size for the scene */
    SKScene *scene = [ZMMyScene sceneWithSize:CGSizeMake(1024, 768)];

    /* Set the scale mode to scale to fit the window */
    [scene setScaleMode: SKSceneScaleModeAspectFit];

    [self.skView presentScene:scene];

    [self.skView setShowsFPS: YES];
    [self.skView setShowsNodeCount: YES];
}

- (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)sender {
    return YES;
}

@end

//
//  ZMMyScene.m
//  Magnets
//
//  Created by zaxdo on 12.04.14.
//  Copyright (c) 2014 zaxdo. All rights reserved.
//

#import "ZMMyScene.h"


enum : NSUInteger {
    kLeftMouseButton = 1<<0,
    kRightMouseButton = 1<<1,
};

@interface ZMMyScene (){
	NSMutableArray *_magnets, *_bodies;
}
@end

static inline CGVector rwSubVec(CGPoint a, CGPoint b) {
    return CGVectorMake(a.x - b.x, a.y - b.y);
}

static inline float rwLengthVec(CGVector a) {
    return sqrtf(a.dx * a.dx + a.dy * a.dy);
}

// Makes a vector have a length of 1
static inline CGVector rwNormalizeVec(CGVector a) {
    float length = rwLengthVec(a);
    return CGVectorMake(a.dx / length, a.dy / length);
}
static inline CGVector rwMulVec(CGVector a, float b) {
    return CGVectorMake(a.dx * b, a.dy * b);
}



@implementation ZMMyScene

-(id)initWithSize:(CGSize)size {    
    if (self = [super initWithSize:size]) {
        self.backgroundColor = [SKColor colorWithRed:0.15 green:0.15 blue:0.3 alpha:1.0];
		_bodies = [NSMutableArray array];
		_magnets = [NSMutableArray array];
		[self.physicsWorld setGravity:(CGVector){0,0}];
        
    }
    return self;
}



-(void)mouseDown:(NSEvent *)event {
	if (self.object == 0) {
		CGPoint location = [event locationInNode:self];

		SKShapeNode *sprite = [[SKShapeNode alloc] init];
		[sprite setPath:CGPathCreateWithEllipseInRect((CGRect){(CGPoint){-25,-25},(CGSize){50,50}}, &CGAffineTransformIdentity)];
		[sprite setStrokeColor:[SKColor redColor]];
		sprite.position = location;
		[_bodies addObject:sprite];
		[sprite setPhysicsBody:[SKPhysicsBody bodyWithRectangleOfSize:(CGSize){50,50}]];
		[self addChild:sprite];
	} else if (self.object == 1) {
		CGPoint location = [event locationInNode:self];

		SKShapeNode *sprite = [[SKShapeNode alloc] init];
		[sprite setPath:CGPathCreateWithRect((CGRect){(CGPoint){-25,-25},(CGSize){50,50}}, &CGAffineTransformIdentity)];
		[sprite setStrokeColor:[SKColor yellowColor]];
		sprite.position = location;
		[_magnets addObject:sprite];
		[self addChild:sprite];

	}


}

-(void)update:(CFTimeInterval)currentTime {
    for (SKShapeNode *magnet in _magnets) {
		for (SKShapeNode *body in _bodies) {
			CGVector dist = rwSubVec(magnet.position, body.position);
			CGVector force = rwMulVec(rwNormalizeVec(dist), 500/rwLengthVec(dist)*self.direction);
			[body.physicsBody applyForce:force];
		}
	}
}

@end

const robot = require('robotjs')
const keyDetector = require('./keyEvent')

robot.setMouseDelay(2);

const moveFrom = (xStart, yStart, xEnd, yEnd) => {

    const xDist = xEnd - xStart
    const yDist = yEnd - yStart
    const step = 75

    for (let i = 0; i < step; i++ ) {
        const {x, y} = robot.getMousePos()
        robot.moveMouse(x + xDist / step, y + yDist / step)
    }

}

const moveToCheckCard = () => {
    robot.moveMouse(963, 1012)
}

const moveLeftRight = (isLeft) => {
    const {x, y} = robot.getMousePos()
    if (isLeft) {
        robot.moveMouse(x - 200, y)
    }else {
        robot.moveMouse(x + 200, y)
    }
}

const allIn = () => {
    robot.moveMouse(1011, 890)
    robot.mouseToggle('down');
    moveFrom(1011, 890, 556, 890)
    moveFrom(556, 890, 1578, 1090)
    moveFrom(1378, 890, 972, 543)
    robot.mouseToggle('up');
}

const summon = () => {
    const {x, y} = robot.getMousePos()
    robot.mouseToggle('down');
    moveFrom(x, y, 972, 543)
    robot.mouseToggle('up');
}

const reset = () => {
    robot.moveMouse(972, 543)
}

const pass = () => {
    robot.moveMouse(1664, 545)
    robot.mouseClick()
}

module.exports = {
    exec: (label) => {
        // if (!keyDetector.getIsPressKey()) return

        console.log(label);
        if (label == "check") moveToCheckCard()
        else if (label == "left" || label == "right") moveLeftRight(label == "left")
        else if (label == "pass") pass()
        else if (label == "allin") allIn()
        else if (label == "in") summon()
        else if (label == "reset") reset()
    }
}
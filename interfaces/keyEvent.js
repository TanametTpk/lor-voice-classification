const ioHook = require('iohook');

class KeyDetector {
    constructor() {
        this.isPressKey = false
    }

    setIsPressKey(status) {
        this.isPressKey = status
    }

    getIsPressKey() {
        return this.isPressKey
    }
}

let keyDetector = new KeyDetector()

ioHook.on("keydown", event => {
    if (event.keycode === 34) {
        console.log("detect");
        keyDetector.setIsPressKey(true)
    }
})

ioHook.on("keyup", event => {
    if (event.keycode === 34) {
        console.log("reles");
        keyDetector.setIsPressKey(false)
    }
})

// ioHook.on("mousedown", event => {
//     if (event.button == 2) {
//         keyDetector.setIsPressKey(true)
//     }
// });

// ioHook.on("mouseup", event => {
//     if (event.button == 2) {
//         keyDetector.setIsPressKey(false)
//     }
// });

ioHook.start();

module.exports = keyDetector
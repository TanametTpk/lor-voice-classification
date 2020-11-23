const robotjs = require('robotjs')

module.exports = {

    getPosition: () => {
        return robotjs.getMousePos()
    }

}
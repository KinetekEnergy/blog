---
toc: True
comments: False
layout: post
title: Javascript Calculator
tags: ['hacks']
categories: ['CSP', 'Week 2']
---

<hr style='solid'>

### JavaScript Calculator

<style>
    /*css grid*/

    .calculator-grid {
        display: grid;
        display: block justify-content: center;
        align-content: center;
        min-height: auto;
        min-width: auto;
        grid-template-columns: repeat(4, 100px);
        grid-template-rows: minmax(120px, auto) repeat(5, 100px);
    }

    /*grid settings for the button*/
    .calculator-grid>button {
        cursor: pointer;
        font-size: 2rem;
        outline: none;
        background-color: #e9e9ed;
        border-radius: 10px;
        border: 0px;
        padding: 5px;
        margin: 5px;

        transition-duration: 0.4s;
    }

    .calculator-grid>button:hover {
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        background-color: #e9e9ed;
    }

    /*span-two is a button with a length of two (AC & DEL)*/
    .span-two {
        grid-column: span 2;
        color: white;
        background-color: #7ea9b1 !important;
    }

    /*couldn't use the span 2, but wanted the color scheme*/
    .equals-button {
        color: #ffffff;
        background-color: #7ea9b1 !important;
    }

    /*the output box at the top*/
    .output {
        grid-column: 1 / -1;
        background-color: rgba(0, 0, 0, 0.75);
        display: flex;
        align-items: flex-end;
        justify-content: space-around;
        flex-direction: column;
        word-wrap: break-word;
        word-break: break-all;

        border-radius: 10px;
        border: 0px;
        padding: 5px;
        padding-right: 10px;
        margin: 5px;
    }

    /*the previous number*/
    .output .previous-operand {
        color: rgba(255, 255, 255, 0.75);
        font-size: 1.5rem;
        animation-name: test;
        animation-duration: 4s;
    }

    /*the current number*/
    .output .current-operand {
        color: white;
        font-size: 2.5rem;
    }
</style>

<div class="calculator-grid">
    <div class="output">
        <div data-previous-operand class="previous-operand"></div>
        <div data-current-operand class="current-operand">Type to begin.</div>
    </div>

    <button data-all-clear class="span-two">AC</button>
    <button data-delete class="span-two">DEL</button>
    <button data-operation>÷</button>
    <button data-number>1</button>
    <button data-number>2</button>
    <button data-number>3</button>
    <button data-operation>*</button>
    <button data-number>4</button>
    <button data-number>5</button>
    <button data-number>6</button>
    <button data-operation>+</button>
    <button data-number>7</button>
    <button data-number>8</button>
    <button data-number>9</button>
    <button data-operation>-</button>
    <button data-number>.</button>
    <button data-number>0</button>
    <button data-equals class="equals-button">=</button>
</div>
<script>
    class Calculator {
        constructor(previousOperandTextElement, currentOperandTextElement) {
            this.previousOperandTextElement = previousOperandTextElement
            this.currentOperandTextElement = currentOperandTextElement
            this.clear()
        }
    

        clear() { //clear window by setting text to null
            this.currentOperand = ''
            this.previousOperand = ''
            this.operation = undefined
        }
    
        delete() { //delete the number
            this.currentOperand = this.currentOperand.toString().slice(0, -1)
        }

        appendNumber(number) { //append numbers so clicking 1, 2, 3, 4, shows 1234
            if (number === '.' && this.currentOperand.includes('.')) return
            this.currentOperand = this.currentOperand.toString() + number.toString()
        }

        chooseOperation(operation) { //choose the operation: +, -, /, *
            if (this.currentOperand === '') return
            if (this.previousOperand !== '') {
                this.compute()
            }
            this.operation = operation
            this.previousOperand = this.currentOperand
            this.currentOperand = ''
        }

        compute() { //computation
            let computation
            const prev = parseFloat(this.previousOperand)
            const current = parseFloat(this.currentOperand)
            if (isNaN(prev) || isNaN(current)) return
            switch (this.operation) {
                case '+':
                    computation = prev + current
                    break
                case '-':
                    computation = prev - current
                    break
                case '*':
                    computation = prev * current
                    break
                case '÷':
                    computation = prev / current
                    break
                default:
                    return
            }
            this.currentOperand = computation
            this.operation = undefined
            this.previousOperand = ''
        }

        getDisplayNumber(number) { //parse display
            const stringNumber = number.toString()
            const integerDigits = parseFloat(stringNumber.split('.')[0])
            const decimalDigits = stringNumber.split('.')[1]
            let integerDisplay
            if (isNaN(integerDigits)) {
                integerDisplay = ''
            } else {
                integerDisplay = integerDigits.toLocaleString('en', { maximumFractionDigits: 0 })
            }
            if (decimalDigits != null) {
                return `${integerDisplay}.${decimalDigits}`
            } else {
                return integerDisplay
            }
        }

        updateDisplay() { //update the display
            this.currentOperandTextElement.innerText =
                this.getDisplayNumber(this.currentOperand)
            if (this.operation != null) {
                this.previousOperandTextElement.innerText =
                    `${this.getDisplayNumber(this.previousOperand)} ${this.operation}`
            } else {
                this.previousOperandTextElement.innerText = ''
            }
        }
    }

    //select buttons
    //querySelectorAll for multiple, querySelector for singles
    const numberButtons = document.querySelectorAll('[data-number]')
    const operationButtons = document.querySelectorAll('[data-operation]')
    const equalsButton = document.querySelector('[data-equals]')
    const deleteButton = document.querySelector('[data-delete]')
    const allClearButton = document.querySelector('[data-all-clear]')
    const previousOperandTextElement = document.querySelector('[data-previous-operand]')
    const currentOperandTextElement = document.querySelector('[data-current-operand]')

    const calculator = new Calculator(previousOperandTextElement, currentOperandTextElement)

    //event listeners for button clicks
    numberButtons.forEach(button => {
        button.addEventListener('click', () => {
            calculator.appendNumber(button.innerText)
            calculator.updateDisplay()
        })
    })

    operationButtons.forEach(button => {
        button.addEventListener('click', () => {
            calculator.chooseOperation(button.innerText)
            calculator.updateDisplay()
        })
    })

    equalsButton.addEventListener('click', button => {
        calculator.compute()
        calculator.updateDisplay()
    })

    allClearButton.addEventListener('click', button => {
        calculator.clear()
        calculator.updateDisplay()
    })

    deleteButton.addEventListener('click', button => {
        calculator.delete()
        calculator.updateDisplay()
    })
</script>

Code below:


```python
%%html
<style>
    /*css grid*/

    .calculator-grid {
        display: grid;
        display: block justify-content: center;
        align-content: center;
        min-height: auto;
        min-width: auto;
        grid-template-columns: repeat(4, 100px);
        grid-template-rows: minmax(120px, auto) repeat(5, 100px);
    }

    /*grid settings for the button*/
    .calculator-grid>button {
        cursor: pointer;
        font-size: 2rem;
        outline: none;
        background-color: #e9e9ed;
        border-radius: 10px;
        border: 0px;
        padding: 5px;
        margin: 5px;

        transition-duration: 0.4s;
    }

    .calculator-grid>button:hover {
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        background-color: #e9e9ed;
    }

    /*span-two is a button with a length of two (AC & DEL)*/
    .span-two {
        grid-column: span 2;
        color: white;
        background-color: #7ea9b1 !important;
    }

    /*couldn't use the span 2, but wanted the color scheme*/
    .equals-button {
        color: #ffffff;
        background-color: #7ea9b1 !important;
    }

    /*the output box at the top*/
    .output {
        grid-column: 1 / -1;
        background-color: rgba(0, 0, 0, 0.75);
        display: flex;
        align-items: flex-end;
        justify-content: space-around;
        flex-direction: column;
        word-wrap: break-word;
        word-break: break-all;

        border-radius: 10px;
        border: 0px;
        padding: 5px;
        padding-right: 10px;
        margin: 5px;
    }

    /*the previous number*/
    .output .previous-operand {
        color: rgba(255, 255, 255, 0.75);
        font-size: 1.5rem;
        animation-name: test;
        animation-duration: 4s;
    }

    /*the current number*/
    .output .current-operand {
        color: white;
        font-size: 2.5rem;
    }
</style>

<div class="calculator-grid">
    <div class="output">
        <div data-previous-operand class="previous-operand"></div>
        <div data-current-operand class="current-operand">Type to begin.</div>
    </div>

    <button data-all-clear class="span-two">AC</button>
    <button data-delete class="span-two">DEL</button>
    <button data-operation>÷</button>
    <button data-number>1</button>
    <button data-number>2</button>
    <button data-number>3</button>
    <button data-operation>*</button>
    <button data-number>4</button>
    <button data-number>5</button>
    <button data-number>6</button>
    <button data-operation>+</button>
    <button data-number>7</button>
    <button data-number>8</button>
    <button data-number>9</button>
    <button data-operation>-</button>
    <button data-number>.</button>
    <button data-number>0</button>
    <button data-equals class="equals-button">=</button>
</div>
<script>
    class Calculator {
        constructor(previousOperandTextElement, currentOperandTextElement) {
            this.previousOperandTextElement = previousOperandTextElement
            this.currentOperandTextElement = currentOperandTextElement
            this.clear()
        }
    

        clear() { //clear window by setting text to null
            this.currentOperand = ''
            this.previousOperand = ''
            this.operation = undefined
        }
    
        delete() { //delete the number
            this.currentOperand = this.currentOperand.toString().slice(0, -1)
        }

        appendNumber(number) { //append numbers so clicking 1, 2, 3, 4, shows 1234
            if (number === '.' && this.currentOperand.includes('.')) return
            this.currentOperand = this.currentOperand.toString() + number.toString()
        }

        chooseOperation(operation) { //choose the operation: +, -, /, *
            if (this.currentOperand === '') return
            if (this.previousOperand !== '') {
                this.compute()
            }
            this.operation = operation
            this.previousOperand = this.currentOperand
            this.currentOperand = ''
        }

        compute() { //computation
            let computation
            const prev = parseFloat(this.previousOperand)
            const current = parseFloat(this.currentOperand)
            if (isNaN(prev) || isNaN(current)) return
            switch (this.operation) {
                case '+':
                    computation = prev + current
                    break
                case '-':
                    computation = prev - current
                    break
                case '*':
                    computation = prev * current
                    break
                case '÷':
                    computation = prev / current
                    break
                default:
                    return
            }
            this.currentOperand = computation
            this.operation = undefined
            this.previousOperand = ''
        }

        getDisplayNumber(number) { //parse display
            const stringNumber = number.toString()
            const integerDigits = parseFloat(stringNumber.split('.')[0])
            const decimalDigits = stringNumber.split('.')[1]
            let integerDisplay
            if (isNaN(integerDigits)) {
                integerDisplay = ''
            } else {
                integerDisplay = integerDigits.toLocaleString('en', { maximumFractionDigits: 0 })
            }
            if (decimalDigits != null) {
                return `${integerDisplay}.${decimalDigits}`
            } else {
                return integerDisplay
            }
        }

        updateDisplay() { //update the display
            this.currentOperandTextElement.innerText =
                this.getDisplayNumber(this.currentOperand)
            if (this.operation != null) {
                this.previousOperandTextElement.innerText =
                    `${this.getDisplayNumber(this.previousOperand)} ${this.operation}`
            } else {
                this.previousOperandTextElement.innerText = ''
            }
        }
    }

    //select buttons
    //querySelectorAll for multiple, querySelector for singles
    const numberButtons = document.querySelectorAll('[data-number]')
    const operationButtons = document.querySelectorAll('[data-operation]')
    const equalsButton = document.querySelector('[data-equals]')
    const deleteButton = document.querySelector('[data-delete]')
    const allClearButton = document.querySelector('[data-all-clear]')
    const previousOperandTextElement = document.querySelector('[data-previous-operand]')
    const currentOperandTextElement = document.querySelector('[data-current-operand]')

    const calculator = new Calculator(previousOperandTextElement, currentOperandTextElement)

    //event listeners for button clicks
    numberButtons.forEach(button => {
        button.addEventListener('click', () => {
            calculator.appendNumber(button.innerText)
            calculator.updateDisplay()
        })
    })

    operationButtons.forEach(button => {
        button.addEventListener('click', () => {
            calculator.chooseOperation(button.innerText)
            calculator.updateDisplay()
        })
    })

    equalsButton.addEventListener('click', button => {
        calculator.compute()
        calculator.updateDisplay()
    })

    allClearButton.addEventListener('click', button => {
        calculator.clear()
        calculator.updateDisplay()
    })

    deleteButton.addEventListener('click', button => {
        calculator.delete()
        calculator.updateDisplay()
    })
</script>
```

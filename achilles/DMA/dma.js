// Dynamic Weighted Moving Average

import {
    isNumber,
    isArray
  } from './common.js'
  
  
  // @param {Number|Array.<Number>} alpha
  export default (data, alpha, noHead) => {
    const {length} = data
  
    if (alpha > 1) {
      return Array(length)
    }
  
    if (alpha === 1) {
      return data.slice()
    }
  
    const isArrayWeight = isArray(alpha)
    const ret = []
  
    let datum
  
    // period `i`
    let i = 0
  
    // `s` is the value of the DWMA at any time period `i`
    let s = 0
  
    // Handles head
    for (; i < length; i ++) {
      datum = data[i]
  
      if (
        isNumber(datum)
        && (
          !isArrayWeight
          || isNumber(datum)
        )
      ) {
        ret[i] = noHead
          ? 0
          : datum
  
        s = datum
        i ++
  
        break
      }
    }
  
    // Dynamic weights: an array of weights
    // Ref:
    // https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average
    // with a dynamic alpha
    if (isArrayWeight) {
    for (; i < length; i++) {
      datum = data[i]
  
      if (isNumber(datum)) {
        const currentAlpha = alpha[i % alpha.length]
        const currentO = 1 - currentAlpha
        s = ret[i] = currentAlpha * datum + currentO * s
      } else {
        ret[i] = ret[i - 1]
      }
    }
  }
  
    const o = 1 - alpha
  
    // Fixed alpha
    for (; i < length; i ++) {
      datum = data[i]
  
      isNumber(datum)
        ? s = ret[i] = alpha * datum + o * s
        : ret[i] = ret[i - 1]
    }
  
    return ret
  }
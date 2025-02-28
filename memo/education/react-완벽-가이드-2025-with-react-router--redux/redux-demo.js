// yarn add redux
// node redux-demo.js
const redux = require('redux');

const counterReducer = (state = { counter: 0 }, action) => {
  if (action.type === 'increment') {
    return { counter: state.counter + 1 };
  }
  if (action.type === 'decrement') {
    return { counter: state.counter - 1 };
  }
  return state;
};
const store = redux.createStore(counterReducer);

const counterSubscriber = () => {
  const latestState = store.getState();
  console.log('counterSubscriber', latestState);
};

// 위에 정의한 대로 store안의 state 값이 바뀌면 이 구독한 conterSubscriber()를 call 하게 되는 것이다.
store.subscribe(counterSubscriber);

// disptach를 하면 createStore에 등록된 Reducer가 call되게 되며, 여기서 action.type을 보고 값을 변경하게 된다.
store.dispatch({ type: 'increment' });

// 여기서는 해당 사항이 없으므로 값이 변경되지 않는다.  그대로 log를 남기는 것을 보면 print를 하는 것이다. state를 copy하기 때문인가?
store.dispatch({ type: 'others' });

// 📌 Why Does Redux Call Subscribers Even When the State Doesn't Change?
// 1. Redux does not automatically check if the state has changed.
//     - It assumes that the reducer function always returns a new state object, even if nothing has changed.
//     - If the reducer returns the same reference (return state), Redux still notifies all subscribers.
// 2. It's the subscriber's responsibility to check for changes.
//     - Redux does not track previous state inside subscribe().
//     - You need to manually check if the state has actually changed.

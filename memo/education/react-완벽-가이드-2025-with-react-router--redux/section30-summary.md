- description : (education정리) React 완벽 가이드 2025 with React Router & Redux : Section 33. React 요약 및 핵심 정리
- tag : education , summary , my-summary , react

TOC


---------------

# 



# my summary
- useEffect : 1번만 수행
- async / await
- use , useContext : limited global variable
- useReducer , useState : state management
- useImperativeHandle : .??? 으로 보여주는 것.  .open
- createPortal : modal의 위치를 전체 화면 어디엔가 정하기 위해서 사용용
- useRef() : 는 ref의 값으로 넘겨서 해당 object를 가리키게 하기 위한 것이다. ```const dialog = useRef();   <dialog ref={dialog}> ```
- useActionState : ```const [formState, formAction, isSending] = useActionState(checkoutAction,null);```
- useCallback : 함수 인스턴스를 1번만 생성시키게 되어 성능 향상에 도움
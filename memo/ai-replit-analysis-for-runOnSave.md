- description : runOnSave라는 vscode extension에 대한 분석을 replit에 맡긴 결과를 적어놓은 것이다.
- tag : vscode , runOnSave , ai , extension
- date : 2025-01-01

TOC
- [1. VS Code RunOnSave 확장 프로그램 코드 분석:](#1-vs-code-runonsave-확장-프로그램-코드-분석)
  - [1.1. 프로젝트 개요:](#11-프로젝트-개요)
  - [1.2. 주요 파일 구조와 역할:](#12-주요-파일-구조와-역할)
  - [1.3. 실행 흐름: Starting Point](#13-실행-흐름-starting-point)
    - [1.3.1. 주요 동작 과정:](#131-주요-동작-과정)
  - [1.4. 핵심 기능:](#14-핵심-기능)
  - [1.5. 설정 방식:](#15-설정-방식)
- [2. 각 파일별 주요 코드 설명:](#2-각-파일별-주요-코드-설명)
  - [2.1. model.ts:](#21-modelts)
  - [2.2. extension.ts:](#22-extensionts)
  - [2.3. package.json:](#23-packagejson)
  - [2.4. tsconfig.json:](#24-tsconfigjson)
- [분석](#분석)
  - [extention.ts](#extentionts)

------------

- replit : https://replit.com/@cheoljoo/VscodeRunOnSave
- git : https://github.com/emeraldwalk/vscode-runonsave

# 1. VS Code RunOnSave 확장 프로그램 코드 분석:
- 이 확장 프로그램은 파일 저장 이벤트를 기반으로 동작하며, 개발자가 파일 저장 시 자동으로 실행될 작업들을 설정할 수 있게 해주는 유용한 도구입니다.

## 1.1. 프로젝트 개요:
- 이 확장 프로그램은 VS Code에서 파일이 저장될 때마다 특정 명령어를 실행할 수 있게 해주는 도구입니다.
TypeScript로 작성되었으며, VS Code의 확장 API를 사용합니다.
## 1.2. 주요 파일 구조와 역할:
- extension.ts: 확장 프로그램의 메인 파일로, 실행의 시작점입니다.
- model.ts: 타입 정의와 인터페이스를 포함하는 모델 파일입니다.
- package.json: 프로젝트 설정과 의존성을 정의합니다.
## 1.3. 실행 흐름: Starting Point
- 시작점: extension.ts의 activate 함수에서 시작됩니다.
### 1.3.1. 주요 동작 과정:
    - VS Code가 확장을 활성화하면 activate 함수가 호출됨
    - RunOnSaveExtension 클래스의 인스턴스가 생성됨
    - 파일 저장 이벤트(onDidSaveTextDocument)를 감지하여 설정된 명령어를 실행
## 1.4. 핵심 기능:
- 파일 저장 시 설정된 명령어 실행
- 정규식을 통한 파일 매칭
- 동기/비동기 명령어 실행 지원
- 실행 결과를 출력 채널에 표시
## 1.5. 설정 방식:
- VS Code의 settings.json 파일에서 'emeraldwalk.runonsave' 설정을 통해 구성
- 각 명령어는 match 패턴, 실행할 명령어(cmd), 동기/비동기 여부 등을 지정할 수 있음

# 2. 각 파일별 주요 코드 설명:
- extension.ts - 메인 확장 프로그램 로직
- model.ts - 타입 정의
- README.md - 사용자 가이드 문서

## 2.1. model.ts:
```typescript
// Document 타입: VS Code의 TextDocument와 NotebookDocument를 통합하는 유니온 타입
// 두 종류의 문서 모두에서 명령어 실행과 이벤트 처리를 지원하기 위함

// IMessageConfig 인터페이스: 메시지 관련 설정을 정의
// - message: 실행 전 출력할 메시지
// - messageAfter: 실행 후 출력할 메시지
// - showElapsed: 실행 시간 표시 여부

// ICommand 인터페이스: 실행할 명령어의 설정을 정의
// - match: 파일 경로 매칭을 위한 정규식 패턴
// - notMatch: 제외할 파일 경로를 위한 정규식 패턴
// - cmd: 실행할 명령어
// - isAsync: 비동기 실행 여부
// - autoShowOutputPanel: 출력 패널 표시 설정

// IConfig 인터페이스: 전체 확장 프로그램의 설정을 정의
// - shell: 명령어 실행에 사용할 셸
// - autoClearConsole: 콘솔 자동 정리 여부
// - commands: 실행할 명령어 배열

// IExecResult 인터페이스: 명령어 실행 결과를 정의
// - statusCode: 실행 결과 코드
// - elapsedMs: 실행에 걸린 시간
```

## 2.2. extension.ts:
```typescript
// VS Code 확장 프로그램의 주 진입점
// activate 함수: 확장 프로그램이 활성화될 때 호출되는 함수
// - 확장 프로그램 인스턴스 생성
// - 설정 변경 감지 이벤트 등록
// - 명령어 등록 (활성화/비활성화)
// - 파일 저장 이벤트 리스너 등록
// RunOnSaveExtension 클래스: 확장 프로그램의 핵심 로직
// - _runCommands: 명령어 실행을 처리하는 재귀 함수
// - _getExecPromise: 명령어 실행을 위한 Promise 생성
// - _getExecOption: 실행 옵션 설정
// - runCommands: 파일 저장 시 실행될 명령어 처리
// - 기타 유틸리티 메서드들 (설정 로드, 메시지 출력 등)
```

## 2.3. package.json:
```typescript
// 프로젝트 메타데이터 및 설정
// - name, displayName: 확장 프로그램의 이름
// - description: 확장 프로그램 설명
// - version: 버전 정보
// - publisher: 배포자 정보
// - contributes: VS Code에 추가되는 기능 정의
//   - commands: 사용 가능한 명령어 목록
//   - configuration: 확장 프로그램 설정 스키마
// 개발 의존성 정의
// - TypeScript 관련 도구
// - ESLint 설정
// - VS Code 확장 개발 도구
```

## 2.4. tsconfig.json:
```typescript
// TypeScript 컴파일러 설정
// - module: CommonJS 모듈 시스템 사용
// - target: ES6 자바스크립트 버전으로 컴파일
// - outDir: 컴파일된 파일이 저장될 위치
// - sourceMap: 디버깅을 위한 소스맵 생성
```


# 분석
## extention.ts
```typescript
import * as vscode from 'vscode';
import * as path from 'path';
import { exec } from 'child_process';
import type { ICommand, IConfig, IExecResult, Document } from './model';

/**
 * VS Code 확장 프로그램 활성화 시 호출되는 함수
 * 이벤트 리스너와 명령어를 등록하고 초기화를 수행
 */
export function activate(context: vscode.ExtensionContext): void {
  const extension = new RunOnSaveExtension(context);
  extension.showOutputMessage();

  // 설정 변경 시 재로딩
  vscode.workspace.onDidChangeConfiguration(() => {
    const disposeStatus = extension.showStatusMessage(
      '파일 저장 자동 실행: 설정을 다시 불러오는 중...',
    );
    extension.loadConfig();
    disposeStatus.dispose();
  });

  // 확장 기능 활성화 명령어 등록 - 한글 별칭 추가
  vscode.commands.registerCommand(
    'extension.emeraldwalk.enableRunOnSave',
    () => {
      extension.isEnabled = true;
    },
  );
  vscode.commands.registerCommand(
    'runonsave.enable',
    () => {
      extension.isEnabled = true;
    },
  );

  // 확장 기능 비활성화 명령어 등록 - 한글 별칭 추가
  vscode.commands.registerCommand(
    'extension.emeraldwalk.disableRunOnSave',
    () => {
      extension.isEnabled = false;
    },
  );
  vscode.commands.registerCommand(
    'runonsave.disable',
    () => {
      extension.isEnabled = false;
    },
  );

  // 파일 저장 시 이벤트 핸들러 등록
  vscode.workspace.onDidSaveTextDocument((document: vscode.TextDocument) => {
    extension.runCommands(document);
  });

  // 노트북 저장 시 이벤트 핸들러 등록
  vscode.workspace.onDidSaveNotebookDocument((document: vscode.NotebookDocument) => {
    extension.runCommands(document);
  });
}

/**
 * RunOnSave 확장 프로그램의 핵심 클래스
 */
class RunOnSaveExtension {
  private _outputChannel: vscode.OutputChannel;
  private _context: vscode.ExtensionContext;
  private _config: IConfig;

  constructor(context: vscode.ExtensionContext) {
    this._context = context;
    this._outputChannel = vscode.window.createOutputChannel('파일 저장 자동 실행');
    this.loadConfig();
  }

  /**
   * 명령어를 재귀적으로 실행하는 내부 함수
   */
  private async _runCommands(
    commandsOrig: Array<ICommand>,
    document: Document,
  ): Promise<void> {
    const cmds = [...commandsOrig];
    const startMs = performance.now();
    let pendingCount = cmds.length;

    // 명령어 완료 시 호출되는 콜백
    const onCmdComplete = (cfg: ICommand, res: IExecResult) => {
      --pendingCount;
      this.showOutputMessageIfDefined(cfg.messageAfter);
      this.showOutputMessageIfDefined(
        cfg.showElapsed && `실행 시간: ${res.elapsedMs}ms`,
      );

      // 에러 발생 시 출력 패널 표시
      if (cfg.autoShowOutputPanel === 'error' && res.statusCode !== 0) {
        this._outputChannel.show(true);
      }

      // 모든 명령어 실행 완료 시
      if (pendingCount === 0) {
        this.showOutputMessageIfDefined(this._config.messageAfter);
        const totalElapsedMs = performance.now() - startMs;
        this.showOutputMessageIfDefined(
          this._config.showElapsed && `총 실행 시간: ${totalElapsedMs}ms`,
        );
      }
    };

    this.showOutputMessageIfDefined(this._config?.message);

    while (cmds.length > 0) {
      const cfg = cmds.shift();
      this.showOutputMessageIfDefined(cfg.message);

      if (cfg.autoShowOutputPanel === 'always') {
        this._outputChannel.show(true);
      }

      // 명령어가 없는 경우 메시지만 표시
      if (cfg.cmd == null) {
        onCmdComplete(cfg, { elapsedMs: 0, statusCode: 0 });
        continue;
      }

      const cmdPromise = this._getExecPromise(cfg, document);
      const isParallel = cfg.isAsync;

      // 병렬 실행이 필요한 경우
      if (isParallel) {
        void cmdPromise.then((elapsedMs) => {
          onCmdComplete(cfg, elapsedMs);
        });
        continue;
      }

      // 순차 실행이 필요한 경우
      const elapsedMs = await cmdPromise;
      onCmdComplete(cfg, elapsedMs);
    }
  }

  /**
   * 명령어 실행을 위한 Promise 생성
   */
  private _getExecPromise(
    cfg: ICommand,
    document: Document,
  ): Promise<IExecResult> {
    return new Promise((resolve) => {
      const startMs = performance.now();

      const child = exec(cfg.cmd, this._getExecOption(document));
      child.stdout.on('data', (data) => this._outputChannel.append(data));
      child.stderr.on('data', (data) => this._outputChannel.append(data));
      child.on('error', (e) => {
        this.showOutputMessage(e.message);
        resolve({ elapsedMs: performance.now() - startMs, statusCode: 1 });
      });
      child.on('exit', (statusCode) => {
        resolve({ elapsedMs: performance.now() - startMs, statusCode });
      });
    });
  }

  /**
   * 명령어 실행 옵션 설정
   */
  private _getExecOption(document: Document): {
    shell: string;
    cwd: string;
  } {
    return {
      shell: this.shell,
      cwd: this._getWorkspaceFolderPath(document.uri),
    };
  }

  /**
   * 작업 공간 폴더 경로 가져오기
   */
  private _getWorkspaceFolderPath(uri: vscode.Uri) {
    const workspaceFolder = vscode.workspace.getWorkspaceFolder(uri);
    return workspaceFolder
      ? workspaceFolder.uri.fsPath
      : vscode.workspace.rootPath;
  }

  // 확장 기능 활성화 상태 관리
  public get isEnabled(): boolean {
    return !!this._context.globalState.get('isEnabled', true);
  }
  public set isEnabled(value: boolean) {
    this._context.globalState.update('isEnabled', value);
    this.showOutputMessage();
  }

  // 설정된 셸 반환
  public get shell(): string {
    return this._config.shell;
  }

  // 콘솔 자동 정리 설정 반환
  public get autoClearConsole(): boolean {
    return !!this._config.autoClearConsole;
  }

  // 설정된 명령어 목록 반환
  public get commands(): Array<ICommand> {
    return this._config.commands || [];
  }

  /**
   * 설정 로드
   */
  public loadConfig(): void {
    this._config = <IConfig>(
      (<any>vscode.workspace.getConfiguration('emeraldwalk.runonsave'))
    );
  }

  /**
   * 출력 채널에 메시지 표시
   */
  public showOutputMessage(message?: string): void {
    message =
      message || `파일 저장 자동 실행이 ${this.isEnabled ? '활성화' : '비활성화'} 되었습니다.`;
    this._outputChannel.appendLine(message);
  }

  /**
   * 조건부로 출력 채널에 메시지 표시
   */
  public showOutputMessageIfDefined(message?: string | null | false): void {
    if (!message) {
      return;
    }
    this.showOutputMessage(message);
  }

  /**
   * 상태 바와 출력 채널에 메시지 표시
   */
  public showStatusMessage(message: string): vscode.Disposable {
    this.showOutputMessage(message);
    return vscode.window.setStatusBarMessage(message);
  }

  /**
   * 명령어 실행 메인 함수
   */
  public runCommands(document: Document): void {
    if (this.autoClearConsole) {
      this._outputChannel.clear();
    }

    if (!this.isEnabled || this.commands.length === 0) {
      this.showOutputMessage();
      return;
    }

    // 파일 경로 매칭 함수
    const match = (pattern: string) =>
      pattern &&
      pattern.length > 0 &&
      new RegExp(pattern).test(document.uri.fsPath);

    // 실행할 명령어 필터링
    const commandConfigs = this.commands.filter((cfg) => {
      const matchPattern = cfg.match || '';
      const negatePattern = cfg.notMatch || '';

      const isMatch = matchPattern.length === 0 || match(matchPattern);
      const isNegate = negatePattern.length > 0 && match(negatePattern);

      return !isNegate && isMatch;
    });

    if (commandConfigs.length === 0) {
      return;
    }

    // 명령어 매개변수 치환
    const commands: Array<ICommand> = [];
    for (const cfg of commandConfigs) {
      let cmdStr = cfg.cmd;

      const extName = path.extname(document.uri.fsPath);
      const workspaceFolderPath = this._getWorkspaceFolderPath(document.uri);
      const relativeFile = path.relative(
        workspaceFolderPath,
        document.uri.fsPath,
      );

      if (cmdStr) {
        // 각종 매개변수 치환
        cmdStr = cmdStr.replace(/\${file}/g, `${document.uri.fsPath}`);
        cmdStr = cmdStr.replace(/\${workspaceRoot}/g, workspaceFolderPath);
        cmdStr = cmdStr.replace(/\${workspaceFolder}/g, workspaceFolderPath);
        cmdStr = cmdStr.replace(
          /\${fileBasename}/g,
          path.basename(document.uri.fsPath),
        );
        cmdStr = cmdStr.replace(
          /\${fileDirname}/g,
          path.dirname(document.uri.fsPath),
        );
        cmdStr = cmdStr.replace(/\${fileExtname}/g, extName);
        cmdStr = cmdStr.replace(
          /\${fileBasenameNoExt}/g,
          path.basename(document.uri.fsPath, extName),
        );
        cmdStr = cmdStr.replace(/\${relativeFile}/g, relativeFile);
        cmdStr = cmdStr.replace(/\${cwd}/g, process.cwd());

        // 환경 변수 치환
        cmdStr = cmdStr.replace(
          /\${env\.([^}]+)}/g,
          (sub: string, envName: string) => {
            return process.env[envName];
          },
        );
      }

      commands.push({
        message: cfg.message,
        messageAfter: cfg.messageAfter,
        cmd: cmdStr,
        isAsync: !!cfg.isAsync,
        showElapsed: cfg.showElapsed,
        autoShowOutputPanel: cfg.autoShowOutputPanel,
      });
    }

    this._runCommands(commands, document);
  }
}
```
import React from 'react';
import Editor from '@monaco-editor/react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../store/store';
// ... import necessary actions

const CodeEditor: React.FC = () => {
  const dispatch = useDispatch();
  const currentFile = useSelector((state: RootState) => state.project.currentFile);

  const handleEditorChange = (value: string | undefined) => {
    // Dispatch action to update file content
    // dispatch(updateFileContent(value));
  };

  return (
    <div className="code-editor">
      <Editor
        height="90vh"
        language="javascript"
        value={currentFile.content}
        onChange={handleEditorChange}
        theme="vs-dark"
      />
    </div>
  );
};

export default CodeEditor;
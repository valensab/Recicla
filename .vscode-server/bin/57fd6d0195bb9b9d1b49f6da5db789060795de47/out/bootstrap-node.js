"use strict";function setupCurrentWorkingDirectory(){const e=require("path");try{typeof process.env.VSCODE_CWD!="string"&&(process.env.VSCODE_CWD=process.cwd()),process.platform==="win32"&&process.chdir(e.dirname(process.execPath))}catch(t){console.error(t)}}setupCurrentWorkingDirectory(),exports.injectNodeModuleLookupPath=function(e){if(!e)throw new Error("Missing injectPath");const t=require("module"),a=require("path").join(__dirname,"../node_modules"),l=t._resolveLookupPaths;t._resolveLookupPaths=function(n,o){const s=l(n,o);if(Array.isArray(s)){for(let i=0,p=s.length;i<p;i++)if(s[i]===a){s.splice(i,0,e);break}}return s}},exports.removeGlobalNodeModuleLookupPaths=function(){const e=require("module"),t=e.globalPaths,c=e._resolveLookupPaths;e._resolveLookupPaths=function(a,l){const n=c(a,l);let o=0;for(;o<n.length&&n[n.length-1-o]===t[t.length-1-o];)o++;return n.slice(0,n.length-o)}},exports.configurePortable=function(e){const t=require("fs"),c=require("path"),a=c.dirname(__dirname);function l(r){return process.env.VSCODE_DEV?a:process.platform==="darwin"?r.dirname(r.dirname(r.dirname(a))):r.dirname(r.dirname(a))}function n(r){if(process.env.VSCODE_PORTABLE)return process.env.VSCODE_PORTABLE;if(process.platform==="win32"||process.platform==="linux")return r.join(l(r),"data");const u=e.portable||`${e.applicationName}-portable-data`;return r.join(r.dirname(l(r)),u)}const o=n(c),s=!("target"in e)&&t.existsSync(o),i=c.join(o,"tmp"),p=s&&t.existsSync(i);return s?process.env.VSCODE_PORTABLE=o:delete process.env.VSCODE_PORTABLE,p&&(process.platform==="win32"?(process.env.TMP=i,process.env.TEMP=i):process.env.TMPDIR=i),{portableDataPath:o,isPortable:s}};

//# sourceMappingURL=https://ticino.blob.core.windows.net/sourcemaps/57fd6d0195bb9b9d1b49f6da5db789060795de47/core/bootstrap-node.js.map

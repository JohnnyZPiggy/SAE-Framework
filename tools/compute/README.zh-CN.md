# 本地预检与有界 Colab 传输

Issue #66 当前状态：**离线验证通过／五种请求均已真实探测**。已安装 CLI0.7.4
的帮助与 `commands/session.py` 映射确认请求集合为 **T4、L4、G4、H100、A100**；
这不等于账户拥有这些设备。固定测试提交 d4e4185d153976e7b966b7a4a1623c6cf80543cb
上，T4/L4/A100 的身份与传输通过；G4 实际为 RTX PRO6000 Blackwell，按规则
DEVICE_MISMATCH 阻止工作；H100 被服务商拒绝。五次尝试均已停止并完成认证零会话
与最后使用量读回。实际结果见 [独立证据](../../reports/compute-multi-gpu/ENGINEER_HANDOFF.md)。
以下旧 PR48 结果只描述旧版单 T4 请求路径。

分配超时见 [CLI 0.7.4 无分配诊断](diagnostics/README.md)：HTTP 超时与外层进程时限不同，外层超时不能判定 GET/POST 阶段。分配期间不轮询 `status`；它会同步远端 assignments 并可能改写本地会话状态。控制器没有 status 观察循环。

认证可信零会话检查仅支持已审查的 CLI **0.7.4**：复用 `usage` 已认证的只读 `ccu-info` 返回，严格核对完整 balance/rate/assignment count 三行 stdout。分配前要求 count=0 和余额为正；stop 后要求新的可信 count=0 且 stop 成功，余额无需为正。此路径不经过会吞认证退出的 `sync_sessions()`。退出码 0、旧 `sessions` 空列表、仅 stderr 的内容、重复/缺失字段、认证失败、超时或未知 CLI 版本均不能证明释放；失败记 `READBACK_UNVERIFIED` 或 `CLEANUP_FAILED`。继续保留有限清理预算与两次 stop+回读上限，无新增认证管理、API 或供应商文件修改。它依赖受信任的已安装 CLI/服务端响应，不证明回读后的并发账户状态；本地 Mock 不能代替真实端到端验收。

> [English](README.md) | 简体中文

状态：**LOCAL_VALIDATED + SCOPED LIVE_READY（CLI 0.7.4、请求 T4 的纯传输路径）**。固定源码 `8081b6e02eee0754903898d5afe5b112f1bb23d0` 的 [SAE PR #48](https://github.com/JohnnyZPiggy/SAE-Framework/pull/48) 已在真实 Colab 完成 Kernel、driver、文件哈希与 stop 后认证零会话核验；此传输试点未直接观察设备型号。[TorchYAND PR #22](https://github.com/JohnnyZPiggy/TorchYAND/pull/22) 则另行在确认的 Tesla T4 上完成单个算法科学试点，不等于通用加速承诺。基于 SAE_Test PR #3 合并提交提炼；[来源与许可证](NOTICE.md)。只需要相邻的三个 Python 文件、标准库、已有 Git 和 Colab CLI；不提供包发布、后台进程、bootstrap 或 Publisher。数学算法、安装与数值验收属于项目 driver。

未来项目按**精确 SAE 提交或 tag**复制/引用三个运行时文件并保留 MIT 声明，另行记录算法 `--source-sha`。不追踪浮动 main，不升级旧项目 `.sae/`，不强制每次实验复制 90 个协议文档。旧版验证的 Python 版本不等于当前运行环境，当前环境记录在每次报告中。认证读回只接受已审查 CLI0.7.4。默认请求 T4，另接受上文五个已发现的规范型号；未知值在调用 CLI 前报 UNSUPPORTED_DEVICE，防止 CLI 自己把未知名称回退为 A100。CPU/TPU/XLA 与原生编译未实现。

在与实际执行相同的 shell（需要时使用已有 WSL 登录 shell）调用 `--preflight-only --repo-path path/to/project --source-sha 完整40位SHA --run-id 唯一名称 --out 新目录 --cli colab`。它只调用 `version`、本地 Git/文件系统，不认证、不查询会话、不分配资源。使用 Git blob 原始字节导出，忽略脏工作树与 CRLF 转换，临时导出排除 `.sae/`；拒绝符号链接、子模块和不安全路径。临时构建/缓存目录必须可写且位于项目与 Dropbox 外；`--temp-root` 可覆盖。默认不安装；显式 `--install-local` 只用已有 pip/构建依赖进行临时 no-deps 安装，无失败后自动安装或登录。

单独授权的计算任务可去掉 `--preflight-only`，传入项目自己的 `--driver scripts/my_driver.py --artifacts experiments/artifacts.json`。两者从项目精确提交读取，拒绝绝对/越界路径及符号链接，不执行脏文件。driver 临时放在非同步目录，收到 `SAE_CANDIDATE_SHA`；Git 标识 driver 与 manifest 的精确字节，框架不包含算法仓库地址或安装逻辑。

manifest 为 `{"artifacts":[{"name":"measurement.json"}]}`：文件名以 `.json` 结尾，
禁止路径分隔符，远程路径为 `/content/<name>`。框架下载后核对 JSON 的 `source_sha`
和 `status: PASS`，记录本地 SHA-256；不再要求或交叉核对远端 `ARTIFACT` 输出行。
**传输 PASS 不等于科学验收**；必要输出 FAIL 会阻止传输通过，可选 NOT_RUN 信息应放在主报告内，不能伪报通过。

[示例 driver](../../examples/compute_adapter/driver.py) 与 [manifest](../../examples/compute_adapter/artifacts.json) 仅写传输样例，GPU/TPU/编译明确 NOT_RUN。`python -m unittest discover -s tools/compute/tests -v` 会在本地临时目录运行示例及故障回归，无需分配 Colab。

有限默认值仍为总任务5400秒、会话分配窗口600秒、清理保留60秒、Kernel30秒、工作240秒。
各超时须有限且大于零。分配窗口包含整个会话；new 子进程仍最多120秒，
Kernel外层是参数+5秒，工作外层是参数+5秒。最多两次 stop+认证零会话检查；
成功的清理读回记录 balance_after 和 assignments_after。清理未确认则停止型号循环。
CLI余额只有两位小数，是计算单位观测，不是精确收费账单。无购买、充值、订阅或按量计费设置操作。

Kernel输出 KERNEL_REACHABLE 后，输出一行 DEVICE_OBSERVED JSON：通过
`nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader`
读名称、显存、驱动（子进程10秒）；如 torch 可导入，再记录 torch/CUDA 版本、设备0
名称和 capability，不安装 torch。缺失/畸形身份拒绝工作。报告区分 device_requested
与 device_observed，不重新命名实际硬件；G4 请求匹配 RTX PRO 6000，其余请求匹配名称中的家族标记。
不匹配时分类 DEVICE_MISMATCH，默认跳过工作；显式 `--allow-device-mismatch`
可继续，仍保留不匹配分类。
driver还收到 SAE_DEVICE_REQUESTED 和 JSON SAE_DEVICE_OBSERVED 环境字段。

可用单型号 `--device T4`，或互斥的 `--devices T4,L4,G4,H100,A100`。多型号根 run-id
最多35字符，依次建立子目录并写 colab-devices.json；完整分配、探针、工作、下载、
停止、零会话、使用量读回完成后才开始下一型号。分配失败记录
ALLOCATION_FAILED，清理确认后继续其余型号；释放/最后读回不确定则停止循环，
其余 NOT_RUN。既有余额为正和服务商权限仍是前提，计费边界不明时必须
BLOCKED_BILLING_UNCERTAIN；无并发会话、后台重试或新增付费。
操作人中断后完成当前清理即停止序列，不再分配下一型号。
研究任务可显式指定 `--task-seconds 14400 --allocation-seconds 10800
--work-timeout 3600 --cleanup-seconds 120`；预算逐型号生效，始终有限。
本次不改变任何已采用项目的固定协议，后续项目升级 pin 须另行提交。

控制报告保存状态、错误码、源码 SHA、run ID、请求与实际设备、创建与清理状态、前后余额和会话数、下载文件 SHA-256、总时长，以及命令 operation/status/exit_code，不记录原始输出、参数、私人根路径、OAuth URL 或环境转储。下载 artifact 的内容由项目负责，传输层不自动删除其中秘密，独立发布前必须另行检查。工具不写 GitHub。Issue66 已真实核验 GPU 身份与传输；GPU 科学计算、TPU 和编译仍未运行，见[本地证据](../../reports/compute-issue38/summary.md)。完整参数、限制和依赖边界以英文页为准，GPT 独立审核验收与合并。

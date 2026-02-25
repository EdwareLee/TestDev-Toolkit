def compare_test_reports(rep1_path: str, rep2_path: str):
    """
    比较两个测试报告文件，返回用例差异分析结果。
    """
    try:
        with open(rep1_path, "r", encoding="utf-8") as f1:
            set1 = {line.strip() for line in f1 if line.strip()}  # ✅ 统一用 strip
        
        with open(rep2_path, "r", encoding="utf-8") as f2:
            # set2 = {line.strip() for line in f2 if line.strip()}  # ✅
            set2 = set()
            for line in f2:
                cleaned_line = line.strip()
                if cleaned_line:
                    set2.add(cleaned_line)

        return {
            "common": len(set1 & set2),
            "missing_in_rep2": sorted(list(set1 - set2)),
            "new_in_rep2": sorted(list(set2 - set1)),
            "total_rep1": len(set1),
            "total_rep2": len(set2),
        }

    except FileNotFoundError as e:
        return {"error": f"文件未找到: {e.filename}"}  # ✅ key 是 "error"
    except Exception as e:
        return {"error": f"发生错误: {str(e)}"}       # ✅

if __name__ == "__main__":
    result = compare_test_reports("report_old.txt", "report_new.txt")
    if "error" in result:
        print("❌ 错误:", result["error"])
    else:
        print("📊 报告对比结果:")
        print(f"  共同用例数: {result['common']}")
        print(f"  缺失用例 (rep2 中没有): {result['missing_in_rep2']}")
        print(f"  新增用例 (rep2 中有): {result['new_in_rep2']}")